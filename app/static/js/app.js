editorOptions = {
    highlightActiveLine: true,
    maxLines: Infinity,
    fontSize: '0.9rem',
    theme: 'ace/theme/xcode',
    wrap: false,
    indentedSoftWrap: false,
    behavioursEnabled: false,
    showPrintMargin: false
};


if (document.body.id == 'page') {
    const editor = ace.edit('editor');
    const editorContainer = document.getElementById('editor');
    const language = editorContainer.getAttribute('language');
    const btnCopy = document.getElementById('btnCopy');

    editor.setOptions(editorOptions);
    editor.setReadOnly(true);
    editor.setHighlightActiveLine(false);
    editor.setHighlightGutterLine(false);

    editor.renderer.$cursorLayer.element.style.display = 'none'; // Remove cursor
    editor.session.setMode('ace/mode/' + language);
    editor.session.setUseWorker(false);

    editorContainer.style.visibility = 'visible';

    if (language == 'text') {
        editor.setOption('wrap', true)
    }

    btnCopy.addEventListener('click', (event) => {
        const sel = editor.selection.toJSON();
        editor.selectAll();
        editor.focus();
        document.execCommand('copy');
        editor.selection.fromJSON(sel);
    });
}


if (document.body.id == 'index') {
    const editor = ace.edit('editor');
    const editorCounter = document.getElementById('editorCounter');
    const editorError = document.getElementById('editorError');
    const textarea = document.getElementsByName('editor')[0];
    const form = document.getElementById('form');
    const title = document.getElementById('title');
    const languageSelector = document.getElementById('languageSelector');

    editor.setOptions(editorOptions);
    editor.setReadOnly(false);

    const MAX_LENGTH = 16000;
    let currentLength = 0;

    // Check this is /index or /clone page
    const paramsString = document.location.pathname;
    const searchParams = new URLSearchParams(paramsString);
    const isClonePage = searchParams.get('/clone');

    // For /clone page doesn't load values from local storage
    if (isClonePage == null) {
        // Initialise data from localstorage
        let styleValue = localStorage.getItem('attributeStyle');

        if (styleValue) {
            languageSelector.value = styleValue
            editor.session.setMode('ace/mode/' + styleValue);
            // Text wrap only for plane text style
            if (styleValue == 'text') {
                editor.setOption('wrap', true)
            }
        } else {
            // Plane text as default style
            languageSelector.value = 'text'
            editor.session.setMode('ace/mode/text');
            editor.setOption('wrap', true)
        }
    } else { // if page is /Clone
        styleValue = languageSelector.value
        editor.session.setMode('ace/mode/' + styleValue);

        // Text wrap only for plane text style
        if (styleValue == 'text') {
            editor.setOption('wrap', true)
        }
    }
    
    window.onload = function() {
        title.focus();
    };

    languageSelector.addEventListener('change', function() {
        styleValue = languageSelector.value;
        
        if (styleValue == 'text') {
            editor.setOption('wrap', true)
        } else {
            editor.setOption('wrap', false)
        }
        
        editor.session.setMode('ace/mode/' + styleValue);
        localStorage.setItem('attributeStyle', styleValue);
    });

    editor.getSession().on('change', function () {
        textarea.value = editor.getSession().getValue();
        currentLength = editor.session.getValue().length;

        if (currentLength > MAX_LENGTH) {
            editorCounter.textContent = currentLength.toLocaleString() + ' / ' + MAX_LENGTH.toLocaleString();
            editorError.style.visibility = 'visible';

        } else {
            editorError.style.visibility = 'hidden';
        }
    });

    form.addEventListener('submit', (event) => {
        const checkValidity = form.checkValidity();

        if (!checkValidity || currentLength > MAX_LENGTH) {
            event.preventDefault();
            event.stopPropagation();

            const titleValue = title.value;
            const editorValue = editor.getSession().getValue();

            if (titleValue == '') {
                title.focus();

            } else if (editorValue == '' || currentLength > MAX_LENGTH) {
                editor.focus();
            }
        }

        form.classList.add('was-validated');
        }, false);
}

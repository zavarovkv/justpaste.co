editorOptions = {
    highlightActiveLine: true,
    maxLines: Infinity,
    fontSize: '0.9rem',
    theme: 'ace/theme/xcode',
    wrap: false,
    indentedSoftWrap: false,
    behavioursEnabled: false
};


if (document.body.id == 'page') {
    const editorContainer = document.getElementById('editor');
    const language = editorContainer.getAttribute('language')
    const btnCopy = document.getElementById('btnCopy')

    const editor = ace.edit('editor');

    editor.setOptions(editorOptions);
    editor.setReadOnly(true);

    editor.session.setMode('ace/mode/' + language);
    editor.session.setUseWorker(false);

    if (language == 'text') {
        editor.setOption('wrap', true)
    }

    editorContainer.style.visibility = 'visible';


    // Save page to history in local storage

    let history = localStorage.getItem('history');

    btnCopy.addEventListener('click', (event) => {
        const sel = editor.selection.toJSON();
        editor.selectAll();
        editor.focus();
        document.execCommand('copy');
        editor.selection.fromJSON(sel);
    });
}


if (document.body.id == 'index') {

    // Initialise ace editor
    const editor = ace.edit('editor');
    editor.setOptions(editorOptions);
    editor.setReadOnly(false);

    // Add text area for submit code to the serverside
    const textarea = document.getElementsByName('editor')[0]

    // Restriction on max length for text in ace editor
    const editorCounter = document.getElementById('editorCounter');
    const editorError = document.getElementById('editorError');
    const MAX_LENGTH = 16000;
    let currentLength = 0;


    const title = document.getElementById('title');
    const languageSelector = document.getElementById('languageSelector');
    const form = document.getElementById('form');

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

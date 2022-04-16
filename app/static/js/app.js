editorOptions = {
    highlightActiveLine: true,
    maxLines: Infinity,
    fontSize: '1rem',
    theme: 'ace/theme/xcode',
    wrap: false,
    indentedSoftWrap: false,
    behavioursEnabled: false
};


if (document.body.id == 'page') {
    const editorLoader = document.getElementById('editorLoader');
    const likelyBtns = document.getElementById('likelyBtns');

    requestURL = '/1234567890123456789012345678901234567890?type=row'
    
    const xhr = new XMLHttpRequest();
    xhr.open('GET', requestURL);
    
    xhr.onload = () => {
        if (xhr.status !== 200) {
            return;
        }
        editorLoader.remove();
        
        var editor = ace.edit('editor');
        editor.setReadOnly(true);
        editor.session.setValue(xhr.response);
        
        likelyBtns.style.display = 'block';
    };
    xhr.send();
}


if (document.body.id == 'index') {
    const editor = ace.edit('editor');
    const textarea = document.getElementsByName('editor')[0]

    editor.setOptions(editorOptions);
    editor.setReadOnly(false);

    const title = document.getElementById('title');
    const btnShare = document.getElementById('btnShare');
    const languageSelector = document.getElementById('languageSelector');
    const form = document.getElementById('form');

    let styleValue = localStorage.getItem('attributeStyle');

    if (styleValue) {
        languageSelector.value = styleValue
        editor.session.setMode('ace/mode/' + styleValue);
        
        if (styleValue == 'text') {
            editor.setOption('wrap', true)
        }
        
    } else {
        languageSelector.value = 'text'
        editor.session.setMode('ace/mode/text');
        editor.setOption('wrap', true)
    }
    
    
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

    btnShare.addEventListener('click', function() {
        code_title = codeTitle.value;
        code_body = editor.getSession().getValue();
        code_style = styleSelector.value;
        
        console.log('title: ' + code_title)
        console.log('body: ' + code_body);
        console.log('style: ' + code_style);
    });

    editor.getSession().on('change', function () {
        textarea.value = editor.getSession().getValue();
    });

    window.onload = function() {
        title.focus();
    };

    form.addEventListener('submit', (event) => {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();

            if (title.value == '') {
                title.focus();
            } else if (editor.getSession().getValue() == '') {
                editor.focus();
            }

        }
        form.classList.add('was-validated');
        }, false);
}

editorOptions = {
    highlightActiveLine: true,
    maxLines: Infinity,
    placeholder: 'Enter text to share here...',
    fontSize: '1rem',
    theme: 'ace/theme/xcode',
    wrap: false,
    indentedSoftWrap: false,
    behavioursEnabled: false
};


if (document.body.id == 'page') {
    var editorLoader = document.getElementById('editorLoader');
    var likelyBtns = document.getElementById('likelyBtns');
    var btnLikelyCopy = document.getElementById('btnLikelyCopy');
    
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
    
    btnLikelyCopy.addEventListener('click', function() {
        window.navigator.clipboard.writeText(window.location.href);
    });
}


if (document.body.id == 'index') {
    var editor = ace.edit('editor');
    
    editor.setOptions(editorOptions);
    editor.setReadOnly(false);
    
    var codeTitle = document.getElementById('codeTitle');
    var codeBody = document.getElementById('editor');
    var btnShare = document.getElementById('btnShare');
    
    var styleSelector = document.getElementById('styleSelector');
    var privateSelector = document.getElementById('privateSelector');
    
    var styleValue = localStorage.getItem('attributeStyle')
    var privateValue = localStorage.getItem('attributePrivate')
    
    if (styleValue) {
        styleSelector.value = styleValue
        editor.session.setMode('ace/mode/' + styleValue);
        
        if (styleValue == 'text') {
            editor.setOption('wrap', true)
        }
        
    } else {
        styleSelector.value = 'text'
        editor.session.setMode('ace/mode/text');
        editor.setOption('wrap', true)
    }
    
    privateSelector.checked = privateValue;
    
    
    styleSelector.addEventListener('change', function() {
        styleValue = styleSelector.value;
        
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
    
    window.onload = function() {
        codeTitle.focus();
    };
}

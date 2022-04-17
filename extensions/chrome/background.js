chrome.action.onClicked.addListener(async (info, tab) => {
    const newURL = "https://easyshare.co/";
    chrome.tabs.create({ url: newURL });
});
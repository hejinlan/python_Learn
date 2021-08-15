function getChromeVersion() {
    var arr = navigator.userAgent.split(' '); 
    var chromeVersion = '';
    for(var i=0;i < arr.length;i++){
        if(/chrome/i.test(arr[i]))
        chromeVersion = arr[i]
    }
    if(chromeVersion){
        return Number(chromeVersion.split('/')[1].split('.')[0]);
    } else {
        return false;
    }
}
if(getChromeVersion()) {
    var version = getChromeVersion();
    if(version < 32) {
        alert('您使用的谷歌浏览器版本过低，为了更好地体验请将浏览器升级到最新版本！');
    }
}
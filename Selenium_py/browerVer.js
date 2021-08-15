getBrowserVersion:function(){
   var agent = navigator.userAgent.toLowerCase();
   var arr=[];
   var Browser="";
   var Bversion="";
   var verinNum=""; 
   //IE
   if(agent.indexOf("msie") > 0){
    var regStr_ie = /msie [\d.]+;/gi ;
     Browser="IE";
     Bversion=""+agent.match(regStr_ie)   
   }
   //firefox
   else if(agent.indexOf("firefox") > 0){ 
    var regStr_ff = /firefox\/[\d.]+/gi;
       Browser="firefox";
       Bversion=""+agent.match(regStr_ff);
   }
   //Chrome
     else if(agent.indexOf("chrome") > 0){
    var regStr_chrome = /chrome\/[\d.]+/gi ;
     Browser="chrome";
     Bversion=""+agent.match(regStr_chrome);
   }
   //Safari
     else if(agent.indexOf("safari") > 0 && agent.indexOf("chrome") < 0){
    var regStr_saf = /version\/[\d.]+/gi ;
     Browser="safari";
     Bversion=""+agent.match(regStr_saf);
   }
   //Opera
     else if(agent.indexOf("opera")>=0){ 
    var regStr_opera = /version\/[\d.]+/gi ;
     Browser="opera";
     Bversion=""+agent.match(regStr_opera);
     }else{
    var browser=navigator.appName;
    if(browser=="Netscape"){
     var version=agent.split(";");
     var trim_Version=version[7].replace(/[ ]/g,"");   
     var rvStr=trim_Version.match(/[\d\.]/g).toString();
     var rv=rvStr.replace(/[,]/g,"");
     Bversion=rv;
     Browser="IE"
    }
     }
     verinNum=(Bversion+"").replace(/[^0-9.]/ig,"");
     arr.push(Browser);
     arr.push(verinNum);
     return arr;
  }
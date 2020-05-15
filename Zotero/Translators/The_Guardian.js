{
        "translatorID":"82f4da09-df7a-4914-8af1-4e5381d49e31",
	        "translatorType":3,
	        "label":"AAA-Guardian",
	        "creator":"Dimitris Kavroudakis",
	        "target":"^http://(?:www\.)guardian.co.uk/",
	        "minVersion":"1.0",
	        "maxVersion":"",
	        "priority":100,
	        "inRepository":true,
	        "lastUpdated":"2009-05-10 00:31:54"
}

function detectWeb(doc, url){ 
	return "newspaperArticle";
}

function doWeb(doc, url) {
var item = new Zotero.Item("newspaperArticle");
var namespace = doc.documentElement.namespaceURI;

var nsResolver = namespace ? function(prefix) {
  return (prefix == 'x') ? namespace : null;
} : null;

var xpath='/html/head/title/text()';
var fullTitle= doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().textContent;

var tok=fullTitle.split("|");
var titlos=trim(   tok[0]  );
var section=trim(   tok[1]  );
var publisher="The Guardian";

xpath='//meta[@name="description"]/@content';
var abstract= doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().value;

xpath='//div[@id="content"]/ul[@class="article-attributes"]/li[@class="byline"]/a';
var author= doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().textContent;

var fullName= author.split(" ");

var d=url.split("/");
var year=d[4];
var month=d[5];
month=chMonth(month);
var day=d[6];
var finalDate=year + "/"+ month +"/" + day;

item.abstract=abstract;
item.date=finalDate;
item.title=titlos;
item.section=section;
item.publisher=publisher;
item.url=url;
item.creators.push({lastName:fullName[1],firstName:fullName[0],creatorType:"author"});
item.complete();
}

//---------------------------------------
function trim(stringToTrim) {
	stringToTrim.replace(/\s+$/,"");
	return stringToTrim.replace(/^\s+/,"");
}

function chMonth(inString){
var m=new Array(12);
m["jan"]="01";
m["feb"]="02";
m["mar"]="03";
m["apr"]="04";
m["may"]="05";
m["jun"]="06";
m["jul"]="07";
m["aug"]="08";
m["sep"]="09";
m["oct"]="10";
m["nov"]="11";
m["dec"]="12";

	return m[inString];
}


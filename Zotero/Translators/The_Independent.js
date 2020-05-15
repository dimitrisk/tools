{
        "translatorID":"4fa9577c-b991-48cc-b794-70a1a841dd2b",
	        "translatorType":3,
	        "label":"AA_Dimitris_Independent",
	        "creator":"Dimitris Kavroudakis",
	        "target":"^http://(?:www\.)independent.co.uk/news/",
	        "minVersion":"1.0.2",
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
	              if (prefix == 'x') return namespace; else return null;
	              } : null;

item.url = url;
item.publicationTitle="The Independent"; 

var xpath='//meta[@name="icx_headline"]/@content';
item.title = doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().value;
item.shortTitle = doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().value;


xpath='//meta[@name="icx_authors"]/@content';
item.authors= doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().value;

xpath='//meta[@name="icx_section"]/@content';
item.section= doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().value;


xpath='//meta[@name="icx_copyright"]/@content';
item.rights= doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().value;

xpath='//meta[@name="icx_pubdate"]/@content';
//item.date = doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().value;

var jim = doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().value;
var year=jim.split("/");
item.date=year[2]+ "/" + year[0] + "/" + year[1];

xpath='//meta[@name="icx_deckheader"]/@content';
item.description= doc.evaluate(xpath, doc, nsResolver,XPathResult.ANY_TYPE, null).iterateNext().value;




item.complete();
}
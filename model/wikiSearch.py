from urllib.parse import quote
from requests import get

from sys import path
path.append("../../MusicMeta")

from utils.constants import *

def wikiSearch(data):
    pageId = wikiRequest(data, False)

    if(pageId != -1):
        return constructWikiPage(pageId)

def wikiRequest(query, nested):
    requestUrl = WIKI_API_URL + quote(query)

    resp = get(requestUrl).json()
    if((nested) | ("suggestion" not in resp["query"]["searchinfo"])):
        return resp["query"]["search"][0]["pageid"]
    elif("suggestion" in resp["query"]["searchinfo"]):
        return wikiRequest(resp["query"]["searchinfo"]["suggestion"], True)
    else:
        return -1
    
def constructWikiPage(pageId):
    requestUrl = WIKI_CURID_URL + str(pageId)

    resp = ""
    while(resp == ""):
        resp = get(requestUrl).text

    if(resp.find("tbody") == -1):
        return "<html><head><title>Page not found</title></head><body>No wiki page was found for this song</body></html>"

    head = resp.split("<head>")[1].split("</head>")[0]
    stylesheets = []

    index = 0
    while ((index < len(head)) & (index != -1)):
        index = head.find("<link rel=\"stylesheet\"", index)
        indexEnd = head.find("/>", index)
        stylesheets.append(head[index:indexEnd + 2].replace('href="/', 'href="' + WIKI_BASE_URL).replace("amp;", ""))
        index = indexEnd

    html = '<html class="client-nojs vector-feature-language-in-header-enabled vector-feature-language-in-main-page-header-disabled vector-feature-language-alert-in-sidebar-enabled vector-feature-sticky-header-disabled vector-feature-page-tools-disabled vector-feature-page-tools-pinned-disabled vector-feature-main-menu-pinned-disabled vector-feature-limited-width-enabled vector-feature-limited-width-content-enabled" lang="en" dir="ltr">\n'
    html += '<head>\n<title>' + str(pageId) + '</title>\n'
    for style in stylesheets:
        html += style + "\n"
    html += '</head>\n'
    html += '<body class="skin-vector skin-vector-search-vue vector-toc-pinned mediawiki ltr sitedir-ltr mw-hide-empty-elt ns-0 ns-subject mw-editable page-Ain_t_No_Other_Man rootpage-Ain_t_No_Other_Man skin-vector-2022 action-view">'
    html += '<style type="text/css">li{display:inline}</style>'
    html += '<table class="infobox" style="border: 0; border-spacing: 0; margin: 0; padding: 0; float: left; font-size: 88\%; line-height: 1.5em; width: 22em;">\n<tbody>\n'
    html += resp.split("<tbody>")[1].split("</tbody>")[0].replace("=\"//upload", "=\"https://upload").replace('="/wiki', '="' + WIKI_BASE_URL + 'wiki')
    html += "</tbody>\n</table>"
    html += '\n</body>\n</html>'

    return html
# Todo:
#   1. get WIKI_API_URL + search query
#   2. check if the response has a better search suggestion, if not go to step 4
#   3. get WIKI_API_URL + suggested search query
#   4. get first hit from responses and retrieve page id
#   5. get https://en.wikipedia.org/?curid={page id}
#   6. filter out the tbody element
#   7. return the html code to the viewcontroller so it can be put in a popup dialog
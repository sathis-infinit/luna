
def skill_websearch(*args):
    from duckduckgo_search import ddg

    def ddgs(query):
    #results is in json access it using results[0|1|2..][title|body|href|..]
        return ddg(query, time='y')
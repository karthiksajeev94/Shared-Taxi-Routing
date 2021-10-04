# IE 537 Course Project
# Shared-taxi Routing

import time
start = time.time()

from collections import defaultdict
from heapq import *

# Parameter k allows to modify the relative importance between probability of passenger pickup and acceptance of long detours
k=500
# Number of pickups in each sqaure of the grid, obtained from the Uber dataset
popDens={"aa":437,"ab":2294,"ac":171,"ad":532,"ae":678,"af":252,"ag":60,"ah":224,"ba":1338,"bb":4648,"bc":1392,"bd":1561,"be":1926,"bf":909,"bg":340,"bh":81,"ca":1775,"cb":4978,"cc":5143,"cd":3203,"ce":3294,"cf":3429,"cg":990,"ch":223,"da":2077,"db":3372,"dc":7249,"dd":6925,"de":4430,"df":6496,"dg":2944,"dh":929,"ea":1605,"eb":5075,"ec":6460,"ed":9020,"ee":6691,"ef":2443,"eg":3386,"eh":1908,"fa":172,"fb":4889,"fc":5595,"fd":4266,"fe":6808,"ff":4068,"fg":3759,"fh":1623,"ga":497,"gb":3394,"gc":5693,"gd":2449,"ge":4904,"gf":4315,"gg":2999,"gh":1963,"ha":160,"hb":4563,"hc":6988,"hd":5257,"he":5240,"hf":4570,"hg":2081,"hh":1912,"ia":75,"ib":4470,"ic":4839,"id":3750,"ie":5062,"if":5157,"ig":2717,"ih":1684,"ja":4,"jb":10729,"jc":4762,"jd":4194,"je":7025,"jf":6973,"jg":3265,"jh":1073,"ka":4,"kb":5371,"kc":5641,"kd":4113,"ke":6906,"kf":5559,"kg":4619,"kh":1881,"la":126,"lb":4009,"lc":2354,"ld":2979,"le":7399,"lf":6493,"lg":6310,"lh":3901,"ma":0,"mb":3065,"mc":3921,"md":1348,"me":5829,"mf":5113,"mg":4553,"mh":3725,"na":0,"nb":2487,"nc":4163,"nd":1439,"ne":8426,"nf":5363,"ng":5449,"nh":6775}

# New edge weights for adjacent squares; separation into diagonal and non-diagonal squares is done later
for i in popDens:
    if popDens[i]!=0:
        popDens[i]=1/(popDens[i]**k)
    else:
        popDens[i] = 1          # to avoid the occurrence of 1/0

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("aa", "ba", popDens["ba"]),
        ("aa", "bb", popDens["bb"] * 1.414),
        ("aa", "ab", popDens["ab"]),
        ("ab", "aa", popDens["aa"]),
        ("ab", "ba", popDens["ba"] * 1.414),
        ("ab", "bb", popDens["bb"]),
        ("ab", "bc", popDens["bc"] * 1.414),
        ("ab", "ac", popDens["ac"]),
        ("ac", "ab", popDens["ab"]),
        ("ac", "bb", popDens["bb"] * 1.414),
        ("ac", "bc", popDens["bc"]),
        ("ac", "bd", popDens["bd"] * 1.414),
        ("ac", "ad", popDens["ad"]),
        ("ad", "ac", popDens["ac"]),
        ("ad", "bc", popDens["bc"] * 1.414),
        ("ad", "bd", popDens["bd"]),
        ("ad", "be", popDens["be"] * 1.414),
        ("ad", "ae", popDens["ae"]),
        ("ae", "ad", popDens["ad"]),
        ("ae", "bd", popDens["bd"] * 1.414),
        ("ae", "be", popDens["be"]),
        ("ae", "bf", popDens["bf"] * 1.414),
        ("ae", "af", popDens["af"]),
        ("af", "ae", popDens["ae"]),
        ("af", "be", popDens["be"] * 1.414),
        ("af", "bf", popDens["bf"]),
        ("af", "bg", popDens["bg"] * 1.414),
        ("af", "ag", popDens["ag"]),
        ("ag", "af", popDens["af"]),
        ("ag", "bf", popDens["bf"] * 1.414),
        ("ag", "bg", popDens["bg"]),
        ("ag", "bh", popDens["bh"] * 1.414),
        ("ag", "ah", popDens["ah"]),
        ("ah", "ag", popDens["ag"]),
        ("ah", "bg", popDens["bg"] * 1.414),
        ("ah", "bh", popDens["bh"]),
        ("ba", "ca", popDens["ca"]),
        ("ba", "cb", popDens["cb"] * 1.414),
        ("ba", "bb", popDens["bb"]),
        ("ba", "ab", popDens["ab"] * 1.414),
        ("ba", "aa", popDens["aa"]),
        ("bb", "ba", popDens["ba"]),
        ("bb", "ca", popDens["ca"] * 1.414),
        ("bb", "cb", popDens["cb"]),
        ("bb", "cc", popDens["cc"] * 1.414),
        ("bb", "bc", popDens["bc"]),
        ("bb", "ac", popDens["ac"] * 1.414),
        ("bb", "ab", popDens["ab"]),
        ("bb", "aa", popDens["aa"] * 1.414),
        ("bc", "bb", popDens["bb"]),
        ("bc", "cb", popDens["cb"] * 1.414),
        ("bc", "cc", popDens["cc"]),
        ("bc", "cd", popDens["cd"] * 1.414),
        ("bc", "bd", popDens["bd"]),
        ("bc", "ad", popDens["ad"] * 1.414),
        ("bc", "ac", popDens["ac"]),
        ("bc", "ab", popDens["ab"] * 1.414),
        ("bd", "bc", popDens["bc"]),
        ("bd", "cc", popDens["cc"] * 1.414),
        ("bd", "cd", popDens["cd"]),
        ("bd", "ce", popDens["ce"] * 1.414),
        ("bd", "be", popDens["be"]),
        ("bd", "ae", popDens["ae"] * 1.414),
        ("bd", "ad", popDens["ad"]),
        ("bd", "ac", popDens["ac"] * 1.414),
        ("be", "bd", popDens["bd"]),
        ("be", "cd", popDens["cd"] * 1.414),
        ("be", "ce", popDens["ce"]),
        ("be", "cf", popDens["cf"] * 1.414),
        ("be", "bf", popDens["bf"]),
        ("be", "af", popDens["af"] * 1.414),
        ("be", "ae", popDens["ae"]),
        ("be", "ad", popDens["ad"] * 1.414),
        ("bf", "be", popDens["be"]),
        ("bf", "ce", popDens["ce"] * 1.414),
        ("bf", "cf", popDens["cf"]),
        ("bf", "cg", popDens["cg"] * 1.414),
        ("bf", "bg", popDens["bg"]),
        ("bf", "ag", popDens["ag"] * 1.414),
        ("bf", "af", popDens["af"]),
        ("bf", "ae", popDens["ae"] * 1.414),
        ("bg", "bf", popDens["bf"]),
        ("bg", "cf", popDens["cf"] * 1.414),
        ("bg", "cg", popDens["cg"]),
        ("bg", "ch", popDens["ch"] * 1.414),
        ("bg", "bh", popDens["bh"]),
        ("bg", "ah", popDens["ah"] * 1.414),
        ("bg", "ag", popDens["ag"]),
        ("bg", "af", popDens["af"] * 1.414),
        ("bh", "bg", popDens["bg"]),
        ("bh", "cg", popDens["cg"] * 1.414),
        ("bh", "ch", popDens["ch"]),
        ("bh", "ah", popDens["ah"]),
        ("bh", "ag", popDens["ag"] * 1.414),
        ("ca", "da", popDens["da"]),
        ("ca", "db", popDens["db"] * 1.414),
        ("ca", "cb", popDens["cb"]),
        ("ca", "bb", popDens["bb"] * 1.414),
        ("ca", "ba", popDens["ba"]),
        ("cb", "ca", popDens["ca"]),
        ("cb", "da", popDens["da"] * 1.414),
        ("cb", "db", popDens["db"]),
        ("cb", "dc", popDens["dc"] * 1.414),
        ("cb", "cc", popDens["cc"]),
        ("cb", "bc", popDens["bc"] * 1.414),
        ("cb", "bb", popDens["bb"]),
        ("cb", "ba", popDens["ba"] * 1.414),
        ("cc", "cb", popDens["cb"]),
        ("cc", "db", popDens["db"] * 1.414),
        ("cc", "dc", popDens["dc"]),
        ("cc", "dd", popDens["dd"] * 1.414),
        ("cc", "cd", popDens["cd"]),
        ("cc", "bd", popDens["bd"] * 1.414),
        ("cc", "bc", popDens["bc"]),
        ("cc", "bb", popDens["bb"] * 1.414),
        ("cd", "cc", popDens["cc"]),
        ("cd", "dc", popDens["dc"] * 1.414),
        ("cd", "dd", popDens["dd"]),
        ("cd", "de", popDens["de"] * 1.414),
        ("cd", "ce", popDens["ce"]),
        ("cd", "be", popDens["be"] * 1.414),
        ("cd", "bd", popDens["bd"]),
        ("cd", "bc", popDens["bc"] * 1.414),
        ("ce", "cd", popDens["cd"]),
        ("ce", "dd", popDens["dd"] * 1.414),
        ("ce", "de", popDens["de"]),
        ("ce", "df", popDens["df"] * 1.414),
        ("ce", "cf", popDens["cf"]),
        ("ce", "bf", popDens["bf"] * 1.414),
        ("ce", "be", popDens["be"]),
        ("ce", "bd", popDens["bd"] * 1.414),
        ("cf", "ce", popDens["ce"]),
        ("cf", "de", popDens["de"] * 1.414),
        ("cf", "df", popDens["df"]),
        ("cf", "dg", popDens["dg"] * 1.414),
        ("cf", "cg", popDens["cg"]),
        ("cf", "bg", popDens["bg"] * 1.414),
        ("cf", "bf", popDens["bf"]),
        ("cf", "be", popDens["be"] * 1.414),
        ("cg", "cf", popDens["cf"]),
        ("cg", "df", popDens["df"] * 1.414),
        ("cg", "dg", popDens["dg"]),
        ("cg", "dh", popDens["dh"] * 1.414),
        ("cg", "ch", popDens["ch"]),
        ("cg", "bh", popDens["bh"] * 1.414),
        ("cg", "bg", popDens["bg"]),
        ("cg", "bf", popDens["bf"] * 1.414),
        ("ch", "cg", popDens["cg"]),
        ("ch", "dg", popDens["dg"] * 1.414),
        ("ch", "dh", popDens["dh"]),
        ("ch", "bh", popDens["bh"]),
        ("ch", "bg", popDens["bg"] * 1.414),
        ("da", "ea", popDens["ea"]),
        ("da", "eb", popDens["eb"] * 1.414),
        ("da", "db", popDens["db"]),
        ("da", "cb", popDens["cb"] * 1.414),
        ("da", "ca", popDens["ca"]),
        ("db", "da", popDens["da"]),
        ("db", "ea", popDens["ea"] * 1.414),
        ("db", "eb", popDens["eb"]),
        ("db", "ec", popDens["ec"] * 1.414),
        ("db", "dc", popDens["dc"]),
        ("db", "cc", popDens["cc"] * 1.414),
        ("db", "cb", popDens["cb"]),
        ("db", "ca", popDens["ca"] * 1.414),
        ("dc", "db", popDens["db"]),
        ("dc", "eb", popDens["eb"] * 1.414),
        ("dc", "ec", popDens["ec"]),
        ("dc", "ed", popDens["ed"] * 1.414),
        ("dc", "dd", popDens["dd"]),
        ("dc", "cd", popDens["cd"] * 1.414),
        ("dc", "cc", popDens["cc"]),
        ("dc", "cb", popDens["cb"] * 1.414),
        ("dd", "dc", popDens["dc"]),
        ("dd", "ec", popDens["ec"] * 1.414),
        ("dd", "ed", popDens["ed"]),
        ("dd", "ee", popDens["ee"] * 1.414),
        ("dd", "de", popDens["de"]),
        ("dd", "ce", popDens["ce"] * 1.414),
        ("dd", "cd", popDens["cd"]),
        ("dd", "cc", popDens["cc"] * 1.414),
        ("de", "dd", popDens["dd"]),
        ("de", "ed", popDens["ed"] * 1.414),
        ("de", "ee", popDens["ee"]),
        ("de", "ef", popDens["ef"] * 1.414),
        ("de", "df", popDens["df"]),
        ("de", "cf", popDens["cf"] * 1.414),
        ("de", "ce", popDens["ce"]),
        ("de", "cd", popDens["cd"] * 1.414),
        ("df", "de", popDens["de"]),
        ("df", "ee", popDens["ee"] * 1.414),
        ("df", "ef", popDens["ef"]),
        ("df", "eg", popDens["eg"] * 1.414),
        ("df", "dg", popDens["dg"]),
        ("df", "cg", popDens["cg"] * 1.414),
        ("df", "cf", popDens["cf"]),
        ("df", "ce", popDens["ce"] * 1.414),
        ("dg", "df", popDens["df"]),
        ("dg", "ef", popDens["ef"] * 1.414),
        ("dg", "eg", popDens["eg"]),
        ("dg", "eh", popDens["eh"] * 1.414),
        ("dg", "dh", popDens["dh"]),
        ("dg", "ch", popDens["ch"] * 1.414),
        ("dg", "cg", popDens["cg"]),
        ("dg", "cf", popDens["cf"] * 1.414),
        ("dh", "dg", popDens["dg"]),
        ("dh", "eg", popDens["eg"] * 1.414),
        ("dh", "eh", popDens["eh"]),
        ("dh", "ch", popDens["ch"]),
        ("dh", "cg", popDens["cg"] * 1.414),
        ("ea", "fa", popDens["fa"]),
        ("ea", "fb", popDens["fb"] * 1.414),
        ("ea", "eb", popDens["eb"]),
        ("ea", "db", popDens["db"] * 1.414),
        ("ea", "da", popDens["da"]),
        ("eb", "ea", popDens["ea"]),
        ("eb", "fa", popDens["fa"] * 1.414),
        ("eb", "fb", popDens["fb"]),
        ("eb", "fc", popDens["fc"] * 1.414),
        ("eb", "ec", popDens["ec"]),
        ("eb", "dc", popDens["dc"] * 1.414),
        ("eb", "db", popDens["db"]),
        ("eb", "da", popDens["da"] * 1.414),
        ("ec", "eb", popDens["eb"]),
        ("ec", "fb", popDens["fb"] * 1.414),
        ("ec", "fc", popDens["fc"]),
        ("ec", "fd", popDens["fd"] * 1.414),
        ("ec", "ed", popDens["ed"]),
        ("ec", "dd", popDens["dd"] * 1.414),
        ("ec", "dc", popDens["dc"]),
        ("ec", "db", popDens["db"] * 1.414),
        ("ed", "ec", popDens["ec"]),
        ("ed", "fc", popDens["fc"] * 1.414),
        ("ed", "fd", popDens["fd"]),
        ("ed", "fe", popDens["fe"] * 1.414),
        ("ed", "ee", popDens["ee"]),
        ("ed", "de", popDens["de"] * 1.414),
        ("ed", "dd", popDens["dd"]),
        ("ed", "dc", popDens["dc"] * 1.414),
        ("ee", "ed", popDens["ed"]),
        ("ee", "fd", popDens["fd"] * 1.414),
        ("ee", "fe", popDens["fe"]),
        ("ee", "ff", popDens["ff"] * 1.414),
        ("ee", "ef", popDens["ef"]),
        ("ee", "df", popDens["df"] * 1.414),
        ("ee", "de", popDens["de"]),
        ("ee", "dd", popDens["dd"] * 1.414),
        ("ef", "ee", popDens["ee"]),
        ("ef", "fe", popDens["fe"] * 1.414),
        ("ef", "ff", popDens["ff"]),
        ("ef", "fg", popDens["fg"] * 1.414),
        ("ef", "eg", popDens["eg"]),
        ("ef", "dg", popDens["dg"] * 1.414),
        ("ef", "df", popDens["df"]),
        ("ef", "de", popDens["de"] * 1.414),
        ("eg", "ef", popDens["ef"]),
        ("eg", "ff", popDens["ff"] * 1.414),
        ("eg", "fg", popDens["fg"]),
        ("eg", "fh", popDens["fh"] * 1.414),
        ("eg", "eh", popDens["eh"]),
        ("eg", "dh", popDens["dh"] * 1.414),
        ("eg", "dg", popDens["dg"]),
        ("eg", "df", popDens["df"] * 1.414),
        ("eh", "eg", popDens["eg"]),
        ("eh", "fg", popDens["fg"] * 1.414),
        ("eh", "fh", popDens["fh"]),
        ("eh", "dh", popDens["dh"]),
        ("eh", "dg", popDens["dg"] * 1.414),
        ("fa", "ga", popDens["ga"]),
        ("fa", "gb", popDens["gb"] * 1.414),
        ("fa", "fb", popDens["fb"]),
        ("fa", "eb", popDens["eb"] * 1.414),
        ("fa", "ea", popDens["ea"]),
        ("fb", "fa", popDens["fa"]),
        ("fb", "ga", popDens["ga"] * 1.414),
        ("fb", "gb", popDens["gb"]),
        ("fb", "gc", popDens["gc"] * 1.414),
        ("fb", "fc", popDens["fc"]),
        ("fb", "ec", popDens["ec"] * 1.414),
        ("fb", "eb", popDens["eb"]),
        ("fb", "ea", popDens["ea"] * 1.414),
        ("fc", "fb", popDens["fb"]),
        ("fc", "gb", popDens["gb"] * 1.414),
        ("fc", "gc", popDens["gc"]),
        ("fc", "gd", popDens["gd"] * 1.414),
        ("fc", "fd", popDens["fd"]),
        ("fc", "ed", popDens["ed"] * 1.414),
        ("fc", "ec", popDens["ec"]),
        ("fc", "eb", popDens["eb"] * 1.414),
        ("fd", "fc", popDens["fc"]),
        ("fd", "gc", popDens["gc"] * 1.414),
        ("fd", "gd", popDens["gd"]),
        ("fd", "ge", popDens["ge"] * 1.414),
        ("fd", "fe", popDens["fe"]),
        ("fd", "ee", popDens["ee"] * 1.414),
        ("fd", "ed", popDens["ed"]),
        ("fd", "ec", popDens["ec"] * 1.414),
        ("fe", "fd", popDens["fd"]),
        ("fe", "gd", popDens["gd"] * 1.414),
        ("fe", "ge", popDens["ge"]),
        ("fe", "gf", popDens["gf"] * 1.414),
        ("fe", "ff", popDens["ff"]),
        ("fe", "ef", popDens["ef"] * 1.414),
        ("fe", "ee", popDens["ee"]),
        ("fe", "ed", popDens["ed"] * 1.414),
        ("ff", "fe", popDens["fe"]),
        ("ff", "ge", popDens["ge"] * 1.414),
        ("ff", "gf", popDens["gf"]),
        ("ff", "gg", popDens["gg"] * 1.414),
        ("ff", "fg", popDens["fg"]),
        ("ff", "eg", popDens["eg"] * 1.414),
        ("ff", "ef", popDens["ef"]),
        ("ff", "ee", popDens["ee"] * 1.414),
        ("fg", "ff", popDens["ff"]),
        ("fg", "gf", popDens["gf"] * 1.414),
        ("fg", "gg", popDens["gg"]),
        ("fg", "gh", popDens["gh"] * 1.414),
        ("fg", "fh", popDens["fh"]),
        ("fg", "eh", popDens["eh"] * 1.414),
        ("fg", "eg", popDens["eg"]),
        ("fg", "ef", popDens["ef"] * 1.414),
        ("fh", "fg", popDens["fg"]),
        ("fh", "gg", popDens["gg"] * 1.414),
        ("fh", "gh", popDens["gh"]),
        ("fh", "eh", popDens["eh"]),
        ("fh", "eg", popDens["eg"] * 1.414),
        ("ga", "ha", popDens["ha"]),
        ("ga", "hb", popDens["hb"] * 1.414),
        ("ga", "gb", popDens["gb"]),
        ("ga", "fb", popDens["fb"] * 1.414),
        ("ga", "fa", popDens["fa"]),
        ("gb", "ga", popDens["ga"]),
        ("gb", "ha", popDens["ha"] * 1.414),
        ("gb", "hb", popDens["hb"]),
        ("gb", "hc", popDens["hc"] * 1.414),
        ("gb", "gc", popDens["gc"]),
        ("gb", "fc", popDens["fc"] * 1.414),
        ("gb", "fb", popDens["fb"]),
        ("gb", "fa", popDens["fa"] * 1.414),
        ("gc", "gb", popDens["gb"]),
        ("gc", "hb", popDens["hb"] * 1.414),
        ("gc", "hc", popDens["hc"]),
        ("gc", "hd", popDens["hd"] * 1.414),
        ("gc", "gd", popDens["gd"]),
        ("gc", "fd", popDens["fd"] * 1.414),
        ("gc", "fc", popDens["fc"]),
        ("gc", "fb", popDens["fb"] * 1.414),
        ("gd", "gc", popDens["gc"]),
        ("gd", "hc", popDens["hc"] * 1.414),
        ("gd", "hd", popDens["hd"]),
        ("gd", "he", popDens["he"] * 1.414),
        ("gd", "ge", popDens["ge"]),
        ("gd", "fe", popDens["fe"] * 1.414),
        ("gd", "fd", popDens["fd"]),
        ("gd", "fc", popDens["fc"] * 1.414),
        ("ge", "gd", popDens["gd"]),
        ("ge", "hd", popDens["hd"] * 1.414),
        ("ge", "he", popDens["he"]),
        ("ge", "hf", popDens["hf"] * 1.414),
        ("ge", "gf", popDens["gf"]),
        ("ge", "ff", popDens["ff"] * 1.414),
        ("ge", "fe", popDens["fe"]),
        ("ge", "fd", popDens["fd"] * 1.414),
        ("gf", "ge", popDens["ge"]),
        ("gf", "he", popDens["he"] * 1.414),
        ("gf", "hf", popDens["hf"]),
        ("gf", "hg", popDens["hg"] * 1.414),
        ("gf", "gg", popDens["gg"]),
        ("gf", "fg", popDens["fg"] * 1.414),
        ("gf", "ff", popDens["ff"]),
        ("gf", "fe", popDens["fe"] * 1.414),
        ("gg", "gf", popDens["gf"]),
        ("gg", "hf", popDens["hf"] * 1.414),
        ("gg", "hg", popDens["hg"]),
        ("gg", "hh", popDens["hh"] * 1.414),
        ("gg", "gh", popDens["gh"]),
        ("gg", "fh", popDens["fh"] * 1.414),
        ("gg", "fg", popDens["fg"]),
        ("gg", "ff", popDens["ff"] * 1.414),
        ("gh", "gg", popDens["gg"]),
        ("gh", "hg", popDens["hg"] * 1.414),
        ("gh", "hh", popDens["hh"]),
        ("gh", "fh", popDens["fh"]),
        ("gh", "fg", popDens["fg"] * 1.414),
        ("ha", "ia", popDens["ia"]),
        ("ha", "ib", popDens["ib"] * 1.414),
        ("ha", "hb", popDens["hb"]),
        ("ha", "gb", popDens["gb"] * 1.414),
        ("ha", "ga", popDens["ga"]),
        ("hb", "ha", popDens["ha"]),
        ("hb", "ia", popDens["ia"] * 1.414),
        ("hb", "ib", popDens["ib"]),
        ("hb", "ic", popDens["ic"] * 1.414),
        ("hb", "hc", popDens["hc"]),
        ("hb", "gc", popDens["gc"] * 1.414),
        ("hb", "gb", popDens["gb"]),
        ("hb", "ga", popDens["ga"] * 1.414),
        ("hc", "hb", popDens["hb"]),
        ("hc", "ib", popDens["ib"] * 1.414),
        ("hc", "ic", popDens["ic"]),
        ("hc", "id", popDens["id"] * 1.414),
        ("hc", "hd", popDens["hd"]),
        ("hc", "gd", popDens["gd"] * 1.414),
        ("hc", "gc", popDens["gc"]),
        ("hc", "gb", popDens["gb"] * 1.414),
        ("hd", "hc", popDens["hc"]),
        ("hd", "ic", popDens["ic"] * 1.414),
        ("hd", "id", popDens["id"]),
        ("hd", "ie", popDens["ie"] * 1.414),
        ("hd", "he", popDens["he"]),
        ("hd", "ge", popDens["ge"] * 1.414),
        ("hd", "gd", popDens["gd"]),
        ("hd", "gc", popDens["gc"] * 1.414),
        ("he", "hd", popDens["hd"]),
        ("he", "id", popDens["id"] * 1.414),
        ("he", "ie", popDens["ie"]),
        ("he", "if", popDens["if"] * 1.414),
        ("he", "hf", popDens["hf"]),
        ("he", "gf", popDens["gf"] * 1.414),
        ("he", "ge", popDens["ge"]),
        ("he", "gd", popDens["gd"] * 1.414),
        ("hf", "he", popDens["he"]),
        ("hf", "ie", popDens["ie"] * 1.414),
        ("hf", "if", popDens["if"]),
        ("hf", "ig", popDens["ig"] * 1.414),
        ("hf", "hg", popDens["hg"]),
        ("hf", "gg", popDens["gg"] * 1.414),
        ("hf", "gf", popDens["gf"]),
        ("hf", "ge", popDens["ge"] * 1.414),
        ("hg", "hf", popDens["hf"]),
        ("hg", "if", popDens["if"] * 1.414),
        ("hg", "ig", popDens["ig"]),
        ("hg", "ih", popDens["ih"] * 1.414),
        ("hg", "hh", popDens["hh"]),
        ("hg", "gh", popDens["gh"] * 1.414),
        ("hg", "gg", popDens["gg"]),
        ("hg", "gf", popDens["gf"] * 1.414),
        ("hh", "hg", popDens["hg"]),
        ("hh", "ig", popDens["ig"] * 1.414),
        ("hh", "ih", popDens["ih"]),
        ("hh", "gh", popDens["gh"]),
        ("hh", "gg", popDens["gg"] * 1.414),
        ("ia", "ja", popDens["ja"]),
        ("ia", "jb", popDens["jb"] * 1.414),
        ("ia", "ib", popDens["ib"]),
        ("ia", "hb", popDens["hb"] * 1.414),
        ("ia", "ha", popDens["ha"]),
        ("ib", "ia", popDens["ia"]),
        ("ib", "ja", popDens["ja"] * 1.414),
        ("ib", "jb", popDens["jb"]),
        ("ib", "jc", popDens["jc"] * 1.414),
        ("ib", "ic", popDens["ic"]),
        ("ib", "hc", popDens["hc"] * 1.414),
        ("ib", "hb", popDens["hb"]),
        ("ib", "ha", popDens["ha"] * 1.414),
        ("ic", "ib", popDens["ib"]),
        ("ic", "jb", popDens["jb"] * 1.414),
        ("ic", "jc", popDens["jc"]),
        ("ic", "jd", popDens["jd"] * 1.414),
        ("ic", "id", popDens["id"]),
        ("ic", "hd", popDens["hd"] * 1.414),
        ("ic", "hc", popDens["hc"]),
        ("ic", "hb", popDens["hb"] * 1.414),
        ("id", "ic", popDens["ic"]),
        ("id", "jc", popDens["jc"] * 1.414),
        ("id", "jd", popDens["jd"]),
        ("id", "je", popDens["je"] * 1.414),
        ("id", "ie", popDens["ie"]),
        ("id", "he", popDens["he"] * 1.414),
        ("id", "hd", popDens["hd"]),
        ("id", "hc", popDens["hc"] * 1.414),
        ("ie", "id", popDens["id"]),
        ("ie", "jd", popDens["jd"] * 1.414),
        ("ie", "je", popDens["je"]),
        ("ie", "jf", popDens["jf"] * 1.414),
        ("ie", "if", popDens["if"]),
        ("ie", "hf", popDens["hf"] * 1.414),
        ("ie", "he", popDens["he"]),
        ("ie", "hd", popDens["hd"] * 1.414),
        ("if", "ie", popDens["ie"]),
        ("if", "je", popDens["je"] * 1.414),
        ("if", "jf", popDens["jf"]),
        ("if", "jg", popDens["jg"] * 1.414),
        ("if", "ig", popDens["ig"]),
        ("if", "hg", popDens["hg"] * 1.414),
        ("if", "hf", popDens["hf"]),
        ("if", "he", popDens["he"] * 1.414),
        ("ig", "if", popDens["if"]),
        ("ig", "jf", popDens["jf"] * 1.414),
        ("ig", "jg", popDens["jg"]),
        ("ig", "jh", popDens["jh"] * 1.414),
        ("ig", "ih", popDens["ih"]),
        ("ig", "hh", popDens["hh"] * 1.414),
        ("ig", "hg", popDens["hg"]),
        ("ig", "hf", popDens["hf"] * 1.414),
        ("ih", "ig", popDens["ig"]),
        ("ih", "jg", popDens["jg"] * 1.414),
        ("ih", "jh", popDens["jh"]),
        ("ih", "hh", popDens["hh"]),
        ("ih", "hg", popDens["hg"] * 1.414),
        ("ja", "ka", popDens["ka"]),
        ("ja", "kb", popDens["kb"] * 1.414),
        ("ja", "jb", popDens["jb"]),
        ("ja", "ib", popDens["ib"] * 1.414),
        ("ja", "ia", popDens["ia"]),
        ("jb", "ja", popDens["ja"]),
        ("jb", "ka", popDens["ka"] * 1.414),
        ("jb", "kb", popDens["kb"]),
        ("jb", "kc", popDens["kc"] * 1.414),
        ("jb", "jc", popDens["jc"]),
        ("jb", "ic", popDens["ic"] * 1.414),
        ("jb", "ib", popDens["ib"]),
        ("jb", "ia", popDens["ia"] * 1.414),
        ("jc", "jb", popDens["jb"]),
        ("jc", "kb", popDens["kb"] * 1.414),
        ("jc", "kc", popDens["kc"]),
        ("jc", "kd", popDens["kd"] * 1.414),
        ("jc", "jd", popDens["jd"]),
        ("jc", "id", popDens["id"] * 1.414),
        ("jc", "ic", popDens["ic"]),
        ("jc", "ib", popDens["ib"] * 1.414),
        ("jd", "jc", popDens["jc"]),
        ("jd", "kc", popDens["kc"] * 1.414),
        ("jd", "kd", popDens["kd"]),
        ("jd", "ke", popDens["ke"] * 1.414),
        ("jd", "je", popDens["je"]),
        ("jd", "ie", popDens["ie"] * 1.414),
        ("jd", "id", popDens["id"]),
        ("jd", "ic", popDens["ic"] * 1.414),
        ("je", "jd", popDens["jd"]),
        ("je", "kd", popDens["kd"] * 1.414),
        ("je", "ke", popDens["ke"]),
        ("je", "kf", popDens["kf"] * 1.414),
        ("je", "jf", popDens["jf"]),
        ("je", "if", popDens["if"] * 1.414),
        ("je", "ie", popDens["ie"]),
        ("je", "id", popDens["id"] * 1.414),
        ("jf", "je", popDens["je"]),
        ("jf", "ke", popDens["ke"] * 1.414),
        ("jf", "kf", popDens["kf"]),
        ("jf", "kg", popDens["kg"] * 1.414),
        ("jf", "jg", popDens["jg"]),
        ("jf", "ig", popDens["ig"] * 1.414),
        ("jf", "if", popDens["if"]),
        ("jf", "ie", popDens["ie"] * 1.414),
        ("jg", "jf", popDens["jf"]),
        ("jg", "kf", popDens["kf"] * 1.414),
        ("jg", "kg", popDens["kg"]),
        ("jg", "kh", popDens["kh"] * 1.414),
        ("jg", "jh", popDens["jh"]),
        ("jg", "ih", popDens["ih"] * 1.414),
        ("jg", "ig", popDens["ig"]),
        ("jg", "if", popDens["if"] * 1.414),
        ("jh", "jg", popDens["jg"]),
        ("jh", "kg", popDens["kg"] * 1.414),
        ("jh", "kh", popDens["kh"]),
        ("jh", "ih", popDens["ih"]),
        ("jh", "ig", popDens["ig"] * 1.414),
        ("ka", "la", popDens["la"]),
        ("ka", "lb", popDens["lb"] * 1.414),
        ("ka", "kb", popDens["kb"]),
        ("ka", "jb", popDens["jb"] * 1.414),
        ("ka", "ja", popDens["ja"]),
        ("kb", "ka", popDens["ka"]),
        ("kb", "la", popDens["la"] * 1.414),
        ("kb", "lb", popDens["lb"]),
        ("kb", "lc", popDens["lc"] * 1.414),
        ("kb", "kc", popDens["kc"]),
        ("kb", "jc", popDens["jc"] * 1.414),
        ("kb", "jb", popDens["jb"]),
        ("kb", "ja", popDens["ja"] * 1.414),
        ("kc", "kb", popDens["kb"]),
        ("kc", "lb", popDens["lb"] * 1.414),
        ("kc", "lc", popDens["lc"]),
        ("kc", "ld", popDens["ld"] * 1.414),
        ("kc", "kd", popDens["kd"]),
        ("kc", "jd", popDens["jd"] * 1.414),
        ("kc", "jc", popDens["jc"]),
        ("kc", "jb", popDens["jb"] * 1.414),
        ("kd", "kc", popDens["kc"]),
        ("kd", "lc", popDens["lc"] * 1.414),
        ("kd", "ld", popDens["ld"]),
        ("kd", "le", popDens["le"] * 1.414),
        ("kd", "ke", popDens["ke"]),
        ("kd", "je", popDens["je"] * 1.414),
        ("kd", "jd", popDens["jd"]),
        ("kd", "jc", popDens["jc"] * 1.414),
        ("ke", "kd", popDens["kd"]),
        ("ke", "ld", popDens["ld"] * 1.414),
        ("ke", "le", popDens["le"]),
        ("ke", "lf", popDens["lf"] * 1.414),
        ("ke", "kf", popDens["kf"]),
        ("ke", "jf", popDens["jf"] * 1.414),
        ("ke", "je", popDens["je"]),
        ("ke", "jd", popDens["jd"] * 1.414),
        ("kf", "ke", popDens["ke"]),
        ("kf", "le", popDens["le"] * 1.414),
        ("kf", "lf", popDens["lf"]),
        ("kf", "lg", popDens["lg"] * 1.414),
        ("kf", "kg", popDens["kg"]),
        ("kf", "jg", popDens["jg"] * 1.414),
        ("kf", "jf", popDens["jf"]),
        ("kf", "je", popDens["je"] * 1.414),
        ("kg", "kf", popDens["kf"]),
        ("kg", "lf", popDens["lf"] * 1.414),
        ("kg", "lg", popDens["lg"]),
        ("kg", "lh", popDens["lh"] * 1.414),
        ("kg", "kh", popDens["kh"]),
        ("kg", "jh", popDens["jh"] * 1.414),
        ("kg", "jg", popDens["jg"]),
        ("kg", "jf", popDens["jf"] * 1.414),
        ("kh", "kg", popDens["kg"]),
        ("kh", "lg", popDens["lg"] * 1.414),
        ("kh", "lh", popDens["lh"]),
        ("kh", "jh", popDens["jh"]),
        ("kh", "jg", popDens["jg"] * 1.414),
        ("la", "ma", popDens["ma"]),
        ("la", "mb", popDens["mb"] * 1.414),
        ("la", "lb", popDens["lb"]),
        ("la", "kb", popDens["kb"] * 1.414),
        ("la", "ka", popDens["ka"]),
        ("lb", "la", popDens["la"]),
        ("lb", "ma", popDens["ma"] * 1.414),
        ("lb", "mb", popDens["mb"]),
        ("lb", "mc", popDens["mc"] * 1.414),
        ("lb", "lc", popDens["lc"]),
        ("lb", "kc", popDens["kc"] * 1.414),
        ("lb", "kb", popDens["kb"]),
        ("lb", "ka", popDens["ka"] * 1.414),
        ("lc", "lb", popDens["lb"]),
        ("lc", "mb", popDens["mb"] * 1.414),
        ("lc", "mc", popDens["mc"]),
        ("lc", "md", popDens["md"] * 1.414),
        ("lc", "ld", popDens["ld"]),
        ("lc", "kd", popDens["kd"] * 1.414),
        ("lc", "kc", popDens["kc"]),
        ("lc", "kb", popDens["kb"] * 1.414),
        ("ld", "lc", popDens["lc"]),
        ("ld", "mc", popDens["mc"] * 1.414),
        ("ld", "md", popDens["md"]),
        ("ld", "me", popDens["me"] * 1.414),
        ("ld", "le", popDens["le"]),
        ("ld", "ke", popDens["ke"] * 1.414),
        ("ld", "kd", popDens["kd"]),
        ("ld", "kc", popDens["kc"] * 1.414),
        ("le", "ld", popDens["ld"]),
        ("le", "md", popDens["md"] * 1.414),
        ("le", "me", popDens["me"]),
        ("le", "mf", popDens["mf"] * 1.414),
        ("le", "lf", popDens["lf"]),
        ("le", "kf", popDens["kf"] * 1.414),
        ("le", "ke", popDens["ke"]),
        ("le", "kd", popDens["kd"] * 1.414),
        ("lf", "le", popDens["le"]),
        ("lf", "me", popDens["me"] * 1.414),
        ("lf", "mf", popDens["mf"]),
        ("lf", "mg", popDens["mg"] * 1.414),
        ("lf", "lg", popDens["lg"]),
        ("lf", "kg", popDens["kg"] * 1.414),
        ("lf", "kf", popDens["kf"]),
        ("lf", "ke", popDens["ke"] * 1.414),
        ("lg", "lf", popDens["lf"]),
        ("lg", "mf", popDens["mf"] * 1.414),
        ("lg", "mg", popDens["mg"]),
        ("lg", "mh", popDens["mh"] * 1.414),
        ("lg", "lh", popDens["lh"]),
        ("lg", "kh", popDens["kh"] * 1.414),
        ("lg", "kg", popDens["kg"]),
        ("lg", "kf", popDens["kf"] * 1.414),
        ("lh", "lg", popDens["lg"]),
        ("lh", "mg", popDens["mg"] * 1.414),
        ("lh", "mh", popDens["mh"]),
        ("lh", "kh", popDens["kh"]),
        ("lh", "kg", popDens["kg"] * 1.414),
        ("ma", "na", popDens["na"]),
        ("ma", "nb", popDens["nb"] * 1.414),
        ("ma", "mb", popDens["mb"]),
        ("ma", "lb", popDens["lb"] * 1.414),
        ("ma", "la", popDens["la"]),
        ("mb", "ma", popDens["ma"]),
        ("mb", "na", popDens["na"] * 1.414),
        ("mb", "nb", popDens["nb"]),
        ("mb", "nc", popDens["nc"] * 1.414),
        ("mb", "mc", popDens["mc"]),
        ("mb", "lc", popDens["lc"] * 1.414),
        ("mb", "lb", popDens["lb"]),
        ("mb", "la", popDens["la"] * 1.414),
        ("mc", "mb", popDens["mb"]),
        ("mc", "nb", popDens["nb"] * 1.414),
        ("mc", "nc", popDens["nc"]),
        ("mc", "nd", popDens["nd"] * 1.414),
        ("mc", "md", popDens["md"]),
        ("mc", "ld", popDens["ld"] * 1.414),
        ("mc", "lc", popDens["lc"]),
        ("mc", "lb", popDens["lb"] * 1.414),
        ("md", "mc", popDens["mc"]),
        ("md", "nc", popDens["nc"] * 1.414),
        ("md", "nd", popDens["nd"]),
        ("md", "ne", popDens["ne"] * 1.414),
        ("md", "me", popDens["me"]),
        ("md", "le", popDens["le"] * 1.414),
        ("md", "ld", popDens["ld"]),
        ("md", "lc", popDens["lc"] * 1.414),
        ("me", "md", popDens["md"]),
        ("me", "nd", popDens["nd"] * 1.414),
        ("me", "ne", popDens["ne"]),
        ("me", "nf", popDens["nf"] * 1.414),
        ("me", "mf", popDens["mf"]),
        ("me", "lf", popDens["lf"] * 1.414),
        ("me", "le", popDens["le"]),
        ("me", "ld", popDens["ld"] * 1.414),
        ("mf", "me", popDens["me"]),
        ("mf", "ne", popDens["ne"] * 1.414),
        ("mf", "nf", popDens["nf"]),
        ("mf", "ng", popDens["ng"] * 1.414),
        ("mf", "mg", popDens["mg"]),
        ("mf", "lg", popDens["lg"] * 1.414),
        ("mf", "lf", popDens["lf"]),
        ("mf", "le", popDens["le"] * 1.414),
        ("mg", "mf", popDens["mf"]),
        ("mg", "nf", popDens["nf"] * 1.414),
        ("mg", "ng", popDens["ng"]),
        ("mg", "nh", popDens["nh"] * 1.414),
        ("mg", "mh", popDens["mh"]),
        ("mg", "lh", popDens["lh"] * 1.414),
        ("mg", "lg", popDens["lg"]),
        ("mg", "lf", popDens["lf"] * 1.414),
        ("mh", "mg", popDens["mg"]),
        ("mh", "ng", popDens["ng"] * 1.414),
        ("mh", "nh", popDens["nh"]),
        ("mh", "lh", popDens["lh"]),
        ("mh", "lg", popDens["lg"] * 1.414),
        ("na", "nb", popDens["nb"]),
        ("na", "mb", popDens["mb"] * 1.414),
        ("na", "ma", popDens["ma"]),
        ("nb", "na", popDens["na"]),
        ("nb", "nc", popDens["nc"]),
        ("nb", "mc", popDens["mc"] * 1.414),
        ("nb", "mb", popDens["mb"]),
        ("nb", "ma", popDens["ma"] * 1.414),
        ("nc", "nb", popDens["nb"]),
        ("nc", "nd", popDens["nd"]),
        ("nc", "md", popDens["md"] * 1.414),
        ("nc", "mc", popDens["mc"]),
        ("nc", "mb", popDens["mb"] * 1.414),
        ("nd", "nc", popDens["nc"]),
        ("nd", "ne", popDens["ne"]),
        ("nd", "me", popDens["me"] * 1.414),
        ("nd", "md", popDens["md"]),
        ("nd", "mc", popDens["mc"] * 1.414),
        ("ne", "nd", popDens["nd"]),
        ("ne", "nf", popDens["nf"]),
        ("ne", "mf", popDens["mf"] * 1.414),
        ("ne", "me", popDens["me"]),
        ("ne", "md", popDens["md"] * 1.414),
        ("nf", "ne", popDens["ne"]),
        ("nf", "ng", popDens["ng"]),
        ("nf", "mg", popDens["mg"] * 1.414),
        ("nf", "mf", popDens["mf"]),
        ("nf", "me", popDens["me"] * 1.414),
        ("ng", "nf", popDens["nf"]),
        ("ng", "nh", popDens["nh"]),
        ("ng", "mh", popDens["mh"] * 1.414),
        ("ng", "mg", popDens["mg"]),
        ("ng", "mf", popDens["mf"] * 1.414),
        ("nh", "ng", popDens["ng"]),
        ("nh", "mh", popDens["mh"]),
        ("nh", "mg", popDens["mg"] * 1.414)

    ]

    print ("Desired path is:")
    path = lambda tup: (*path(tup[1]), tup[0]) if tup else ()
    trail = dijkstra(edges, "ga", "gg")
    print(path(trail[1]))

print("Runtime: ", time.time() - start,"s")
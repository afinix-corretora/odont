import re,html,requests,sys,json,time
URL="https://rede.odontosfera.com.br/RedeCredenciada.aspx?Operadora=422088"
def hidden(h): return {k:html.unescape(v) for k,v in re.findall(r'<input type="hidden" name="([^"]+)"[^>]*value="([^"]*)"',h)}
def opts(h,i):
    m=re.search(r'<select[^>]*id="%s".*?</select>'%i,h,re.S); return {html.unescape(c).strip():v for v,c in re.findall(r'<option[^>]*value="([^"]*)"[^>]*>([^<]*)',m.group(0))}
def contar(uf,cid):
    s=requests.Session(); s.headers["User-Agent"]="Mozilla/5.0"
    h=s.get(URL,timeout=60).text; ufv=opts(h,"ddlEstado")[uf]
    f=hidden(h); f.update({"__EVENTTARGET":"ddlEstado","ddlEstado":ufv}); h2=s.post(URL,data=f,timeout=60).text
    base={"ddlEstado":ufv,"ddlCidade":opts(h2,"ddlCidade")[cid],"ddlRegiao":"","ddlBairro":"","ddlExibir":"","ddlPlano":"","ddlTipoEstabelecimento":""}
    f=hidden(h2); f.update(base); f["btBuscar"]="Buscar"; h3=s.post(URL,data=f,timeout=90).text
    names=set(); page=1
    while True:
        cards=re.findall(r'class="modal fade',h3); 
        for m in re.finditer(r'CRO/CNPJ:\|?\s*([\d./-]+)',re.sub(r'<[^>]+>','|',h3)): names.add(m.group(1))
        # next page
        nxt=re.search(r"id=\"ctl_hidden_pag(\d+)(fim)?\" href=\"javascript:__doPostBack\('(ctl_hidden_pag\d+(?:fim)?)'",h3)
        links=re.findall(r'value=(\d+);" id="(ctl_hidden_pag\d+(?:fim)?)"',h3)
        nextp=[l for l in links if int(l[0])==page+1]
        if not nextp or page>60: break
        f=hidden(h3); f.update(base); f["__EVENTTARGET"]=nextp[0][1]; f["ctl_hidden"]=str(page+1); f["ctl_pagina"]=str(page)
        h3=s.post(URL,data=f,timeout=90).text; page+=1
    return len(names),page
for arg in sys.argv[1:]:
    uf,cid=arg.split(':'); n,p=contar(uf,cid); print(f"{cid} ({uf}): {n} prestadores em {p} páginas",flush=True)

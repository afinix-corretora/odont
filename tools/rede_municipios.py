import re,html,requests,sys,json
URL="https://rede.odontosfera.com.br/RedeCredenciada.aspx?Operadora=422088"
s=requests.Session(); s.headers["User-Agent"]="Mozilla/5.0"
def hidden(h):
    return {k:html.unescape(v) for k,v in re.findall(r'<input type="hidden" name="([^"]+)"[^>]*value="([^"]*)"',h)}
r=s.get(URL,timeout=60); h=r.text
states=dict(re.findall(r'<option[^>]*value="([^"]*)"[^>]*>([^<]*)',re.search(r'<select[^>]*id="ddlEstado".*?</select>',h,re.S).group(0)))
states={v:k for k,v in states.items() if k}
print(json.dumps(states,ensure_ascii=False)[:300])
target=sys.argv[1:] or ["MARANHAO"]
out={}
for st in target:
    f=hidden(h); f.update({"__EVENTTARGET":"ddlEstado","ddlEstado":states[st]})
    r2=s.post(URL,data=f,timeout=60); h2=r2.text
    m=re.search(r'<select[^>]*id="ddlCidade".*?</select>',h2,re.S)
    cities=[html.unescape(c).strip() for v,c in re.findall(r'<option[^>]*value="([^"]*)"[^>]*>([^<]*)',m.group(0)) if v]
    out[st]=cities; print(st,len(cities),cities[:12])
json.dump(out,open('cidades.json','w'),ensure_ascii=False)

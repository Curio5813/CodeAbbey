"""
=================
Matching Brackets
=================

We are given strings containing brackets of 4 types - round (), square [], curly {} and angle <> ones.
The goal is to check, whether brackets are in correct sequence. I.e. any opening bracket should have
closing bracket of the same type somewhere further by the string, and bracket pairs should not overlap,
though they could be nested:

(a+[b*c] - {d/3})  - here square and curly brackets are nested in the round ones

(a+[b*c) - 17]     - here square brackets overlap with round ones which does not make sense
Input data will contain number of testcases in the first line.
Then specified number of lines will follow each containing a test-case in form of a character sequence.
Answer should contain 1 (if bracket order is correct) or 0 (if incorrect) for each of test-cases,
separated by spaces.

Example:

input data:
4
(a+[b*c]-{d/3})
(a + [b * c) - 17]
(((a * x) + [b] * y) + c
auf(zlo)men [gy<psy>] four{s}

answer:
1 0 0 1

Note that all non-bracket characters could be safely ignored!
"""

print('')
v1 = ['(*){%}[<z>[f(u>]{<t[v(c)(x)]>v}h]<)<a>(x[-]{([z]^<^>)(y){-}*})',
      '{g}(<*>h( )<b> <({w}{[c<->]c}d)<u>{d}+>[[+][/]f][t][]{ [t]}',
      '<t>[b(t)](^<a>)>[c[h(t)]<t[b]{ }>]<u{w}[c]{w}[]',
      '<>( )[^](([*]g){v}u)<a>[w( )]{/}{[g]<h>w}',
      '<(+)%>[({g}[ <u>{c}][g][+]^[y])v]({/})<{e}</>{a} >',
      '<+>((e(v))[v][/[-]]h)<({<x> }{^}z-[<<b>u[w]>f][x][g[<x>)]]>',
      '(< {b}>{{u}%}){ }[-((- f(y){<%>v}(w))][*]',
      '[b]<f>(w)<((/> {u<u>})<d)[[{c}g]f]{y[ ]}>',
      '(h{ }){<u>{d}(w{{/}t}{^}(a))[(/) (b)]<g{c<<b>/>}[b](^ >}<x>(t)',
      '{% c)}<h>[[(b{-})%<(< >>{^}[-](e){f}](^)]',
      '<(z)x>(z)[( ) ][/](f)[^{v}][ [d]] w>{{g}}',
      '{(e{ }){*} }[(u][g)^(^)](x){-}(<{ }h<v>(x)[ ]>g){}',
      '(({z}t)( )a(c{b})[c({w}[w[e]][ ]/)] <{^}><u>{y}</>',
      '[[v]]<<x>[]y(g){/}((%)a)<<t>^<g>>c>[b](t)',
      '(<e>u)<(d)%>[h{h}(*)[ ]](<d>)<c>(^)<- (v)<<[x]%>/({a}f)>(<e>f)',
      '{{{{{ }[*][%]{z}( )v}g}[a]t}(g)( )}<%><h{t}>',
      '{{x<g>}<<w(+)>e>[g](w{/}){g}({(u)w}{^<d>}h{<f>(^)e}<z>)}',
      '}[([ ](-)< > (c)[f])g{y{{v}(z)]</><g>}(f)[d](f{w})</>',
      '<[b]h><(<<x>{h<v>(d)<a>[ [g]]}(x(g))t> (v[t<+(y)>]{f}))>]']


parentese_aberto = 0
parentese_fechado = 0
colchete_aberto = 0
colchete_fechado = 0
chave_aberto = 0
chave_fechado = 0
menor = 0
maior = 0
v2 = []
resposta = 0
for i in range(0, len(v1)):
    for k, v in enumerate(v1[i]):
        pa = v1.count('(')
        pf = v2.count(')')
        if pa == pf:
            reposta = 1
print(v2)
for i in range(0, len(v2)):
    print(v2[i], end=' ')
print('')
print('')

"""
Utilizar indexação e quantidade de brackets.

(([a + %] + r))
(([a + %) + r])
"""


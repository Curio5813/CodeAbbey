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
brackets = ['{ }[u][{<->[+]t<z>(d{b})}{c}][g( {{z}b})[{c}^][e](b[t])]',
            '<({v}-)<{*}u{%}{v}[t(e)[x]]>[t]{{<{b}{/}%>w}*[{a}v]<^(<u>>%)}>',
            '(t)[<<y>[(y){((+)y{f}) b]^}g( ){(g)[-]<y<z>({e}y)>y}{t}](a)/>]<a>',
            '{u}[+]<x>{v}{}</(^)>[%]{%{<{ }w{ }>g< >}}( {g})',
            '[%]({<(t) >{<(^%}a)/>z({)(%)}(t)[w]{%}%[+]}(g)){((x)e)[[c]h]v}<e>',
            '[y]<y>{ }[( )((e)g){y}(w)<w{c}>w]<<w><t<h >>[w]',
            '{}[[/]<[{f}*]t( )>{ }x(d)](+)[v][b]<e>{v[*]}< ({x}% >[(<h>a)f[^]]',
            '[(+)[%]{-}](w{ [h](f)})^c[t][w]}<{+< >(x)}v>[{<f{^}> }<{> ]</[ ]>',
            '[((y[h))c)(x]]<((+<w>)<b>(^)h)[^]-><b>{a}',
            '(<[x]a u>>y)[{e}[<a>{-}<<-> >e(+)][a]u]( {y}{t}){{h}{%}}[ ]',
            '<(x)[ ]<f><{x}{/}{ }+{-}>*><g{^}>[/](z)<^>[]<+>',
            '{z}[u]()[<x></>(^(b))[(g( ))(u)z(u)] ]{f}',
            '(c[-]<*>{%}){g(y)(w<z>)}{({y} {+})<(e)*[z]>{a}<%>[([-] )[^]a(e)]}',
            '(c)<(v)><c[g<(h{+})>([d](v)(t< ><%>[u]<z[g]>(t)]%>)<g> )[y]',
            '{{v}({{d}+}x)}[<a>{   ][%{(u<</>*>)y}{e}{g}]',
            '{ }<<v></>>(+)a}{w}{ }><[<v>[t][ ](^)x(*<{^}v{)]<c>[a]h<^>>',
            '{z}{<{d}{v}z<a [y]>{t}z}()[w]{c(<->{u}{d}b)(g{-}{%}(w))}[v]',
            '[{z}{[[c]c]{ }<+><[<+>)]d>y}[b](f)</{(e)g}{/}(c)>](d[%])(hz',
            '[h][g][(f[*]<w>(f))-][( )*][v[d](e)[*{*}[y]<t>]]()',
            '[[w](d){^}][{^<^{d}>}g[a{{/}(c)+(<x>+)(f)[y<u>]{d}}]]']
analisys = []
respostas1 = []
respostas2 = []
respostas3 = []
respostas4 = []
respostas5 = []
respostas6 = []
respostas7 = []
respostas8 = []
respostas9 = []
respostas10 = []
resposta = 0
solucoes = []

for k in range(0, len(brackets)):
    res1 = filter(lambda valor: valor == '(' or valor == ')' or valor == '[' or valor == ']', brackets[k])
    brackets1 = list(res1)
    analisys.append(brackets1)
    res2 = filter(lambda valor: valor == '(' or valor == ')' or valor == '{' or valor == '}', brackets[k])
    brackets2 = list(res2)
    analisys.append(brackets2)
    res3 = filter(lambda valor: valor == '(' or valor == ')' or valor == '<' or valor == '>', brackets[k])
    brackets3 = list(res3)
    analisys.append(brackets3)
    res4 = filter(lambda valor: valor == '[' or valor == ']' or valor == '{' or valor == '}', brackets[k])
    brackets4 = list(res4)
    analisys.append(brackets4)
    res5 = filter(lambda valor: valor == '[' or valor == ']' or valor == '<' or valor == '>', brackets[k])
    brackets5 = list(res5)
    analisys.append(brackets5)
    res6 = filter(lambda valor: valor == '{' or valor == '}' or valor == '<' or valor == '>', brackets[k])
    brackets6 = list(res6)
    analisys.append(brackets6)
    res7 = filter(lambda valor: valor == '(' or valor == ')', brackets[k])
    brackets7 = list(res7)
    analisys.append(brackets7)
    res8 = filter(lambda valor: valor == '[' or valor == ']', brackets[k])
    brackets8 = list(res8)
    analisys.append(brackets8)
    res9 = filter(lambda valor: valor == '{' or valor == '}', brackets[k])
    brackets9 = list(res9)
    analisys.append(brackets9)
    res10 = filter(lambda valor: valor == '<' or valor == '>', brackets[k])
    brackets10 = list(res10)
    analisys.append(brackets10)
print(analisys[0])
for m in range(0, len(analisys), 10):
    k = 0
    while k < len(analisys[k]):
        if analisys[k] == '(' and analisys[k + 1] == ']' or analisys[k] == '[' and analisys[k + 1] == ')':
            resposta = 0
        if analisys[k] == '(' and analisys[k + 1] == '(' and analisys[k + 2] == ')' and analisys[k + 3] == '[':
            resposta = 0
        if analisys[k] == '(' and analisys[k + 1] == '(' and analisys[k + 2] == ')' and analisys[k + 3] == ']':
            resposta = 0
        if analisys[k] == ')' and analisys[k + 1] == ')' and analisys[k + 2] == '(' and analisys[k + 3] == '[':
            resposta = 0
        if analisys[k] == ')' and analisys[k + 1] == ')' and analisys[k + 2] == '(' and analisys[k + 3] == ']':
            resposta = 0
        if analisys[k] == '[' and analisys[k + 1] == '[' and analisys[k + 2] == ']' and analisys[k + 3] == '(':
            resposta = 0
        if analisys[k] == '[' and analisys[k + 1] == '[' and analisys[k + 2] == ']' and analisys[k + 3] == ')':
            resposta = 0
        if analisys[k] == ']' and analisys[k + 1] == ']' and analisys[k + 2] == '[' and analisys[k + 3] == '(':
            resposta = 0
        if analisys[k] == ']' and analisys[k + 1] == ']' and analisys[k + 2] == '[' and analisys[k + 3] == ')':
            resposta = 0
        else:
            resposta = 1
        k += 1
    respostas1.append(resposta)
print(respostas1)
for m in range(1, len(analisys), 10):
    k = 0
    while k < len(analisys[k]):
        if analisys[k] == '(' and analisys[k + 1] == '}' or analisys[k] == '{' and analisys[k + 1] == ')':
            resposta = 0
        if analisys[k] == '(' and analisys[k + 1] == '(' and analisys[k + 2] == ')' and analisys[k + 3] == '{':
            resposta = 0
        if analisys[k] == '(' and analisys[k + 1] == '(' and analisys[k + 2] == ')' and analisys[k + 3] == '}':
            resposta = 0
        if analisys[k] == ')' and analisys[k + 1] == ')' and analisys[k + 2] == '(' and analisys[k + 3] == '{':
            resposta = 0
        if analisys[k] == ')' and analisys[k + 1] == ')' and analisys[k + 2] == '(' and analisys[k + 3] == '}':
            resposta = 0
        if analisys[k] == '{' and analisys[k + 1] == '{' and analisys[k + 2] == '}' and analisys[k + 3] == ')':
            resposta = 0
        if analisys[k] == '{' and analisys[k + 1] == '{' and analisys[k + 2] == '}' and analisys[k + 3] == '(':
            resposta = 0
        if analisys[k] == '}' and analisys[k + 1] == '}' and analisys[k + 2] == '{' and analisys[k + 3] == ')':
            resposta = 0
        if analisys[k] == '}' and analisys[k + 1] == '}' and analisys[k + 2] == '{' and analisys[k + 3] == '(':
            resposta = 0
        else:
            resposta = 1
        k += 1
    respostas2.append(resposta)
print(respostas2)
for m in range(2, len(analisys), 10):
    k = 0
    while k < len(analisys[k]):
        if analisys[k] == '(' and analisys[k + 1] == '>' or analisys[k] == '<' and analisys[k + 1] == ')':
            resposta = 0
        if analisys[k] == '(' and analisys[k + 1] == '(' and analisys[k + 2] == ')' and analisys[k + 3] == '<':
            resposta = 0
        if analisys[k] == '(' and analisys[k + 1] == '(' and analisys[k + 2] == ')' and analisys[k + 3] == '>':
            resposta = 0
        if analisys[k] == ')' and analisys[k + 1] == ')' and analisys[k + 2] == '(' and analisys[k + 3] == '<':
            resposta = 0
        if analisys[k] == ')' and analisys[k + 1] == ')' and analisys[k + 2] == '(' and analisys[k + 3] == '>':
            resposta = 0
        if analisys[k] == '<' and analisys[k + 1] == '<' and analisys[k + 2] == '>' and analisys[k + 3] == '(':
            resposta = 0
        if analisys[k] == '<' and analisys[k + 1] == '<' and analisys[k + 2] == '>' and analisys[k + 3] == ')':
            resposta = 0
        if analisys[k] == '>' and analisys[k + 1] == '>' and analisys[k + 2] == '<' and analisys[k + 3] == '(':
            resposta = 0
        if analisys[k] == '>' and analisys[k + 1] == '>' and analisys[k + 2] == '<' and analisys[k + 3] == ')':
            resposta = 0
        else:
            resposta = 1
        k += 1
    respostas3.append(resposta)
print(respostas3)
for m in range(3, len(analisys), 10):
    k = 0
    while k < len(analisys[k]):
        if analisys[k] == '[' and analisys[k + 1] == '}' or analisys[k] == '{' and analisys[k + 1] == ']':
            resposta = 0
        if analisys[k] == '[' and analisys[k + 1] == '[' and analisys[k + 2] == ']' and analisys[k + 3] == '{':
            resposta = 0
        if analisys[k] == '[' and analisys[k + 1] == '[' and analisys[k + 2] == ']' and analisys[k + 3] == '}':
            resposta = 0
        if analisys[k] == ']' and analisys[k + 1] == ']' and analisys[k + 2] == '[' and analisys[k + 3] == '{':
            resposta = 0
        if analisys[k] == ']' and analisys[k + 1] == ']' and analisys[k + 2] == '[' and analisys[k + 3] == '}':
            resposta = 0
        if analisys[k] == '{' and analisys[k + 1] == '{' and analisys[k + 2] == ']' and analisys[k + 3] == '[':
            resposta = 0
        if analisys[k] == '{' and analisys[k + 1] == '{' and analisys[k + 2] == ']' and analisys[k + 3] == ']':
            resposta = 0
        if analisys[k] == '}' and analisys[k + 1] == '}' and analisys[k + 2] == '[' and analisys[k + 3] == '[':
            resposta = 0
        if analisys[k] == '}' and analisys[k + 1] == '}' and analisys[k + 2] == '[' and analisys[k + 3] == ']':
            resposta = 0
        else:
            resposta = 1
        k += 1
    respostas4.append(resposta)
print(respostas4)

"""
for k in range(4, len(analisys), 10):
    if analisys[k] == '[' and analisys[k + 1] == '>' or analisys[k] == '<' and analisys[k + 1] == ']':
        resposta = 0
    if analisys[k] == '[' and analisys[k + 1] == '[' and analisys[k + 2] == ']' and analisys[k + 3] == '<':
        resposta = 0
    if analisys[k] == '[' and analisys[k + 1] == '[' and analisys[k + 2] == ']' and analisys[k + 3] == '>':
        resposta = 0
    if analisys[k] == ']' and analisys[k + 1] == ']' and analisys[k + 2] == '[' and analisys[k + 3] == '<':
        resposta = 0
    if analisys[k] == ']' and analisys[k + 1] == ']' and analisys[k + 2] == '[' and analisys[k + 3] == '>':
        resposta = 0
    else:
        resposta = 1
    respostas5.append(resposta)
for k in range(5, len(analisys), 10):
    if analisys[k] == '{' and analisys[k + 1] == '>' or analisys[k] == '<' and analisys[k + 1] == '}':
        resposta = 0
    if analisys[k] == '{' and analisys[k + 1] == '{' and analisys[k + 2] == '}' and analisys[k + 3] == '<':
        resposta = 0
    if analisys[k] == '{' and analisys[k + 1] == '{' and analisys[k + 2] == '}' and analisys[k + 3] == '>':
        resposta = 0
    if analisys[k] == '}' and analisys[k + 1] == '}' and analisys[k + 2] == '{' and analisys[k + 3] == '<':
        resposta = 0
    if analisys[k] == '}' and analisys[k + 1] == '}' and analisys[k + 2] == '{' and analisys[k + 3] == '>':
        resposta = 0
    else:
        resposta = 1
    respostas6.append(resposta)
for k in range(6, len(analisys), 10):
    if analisys[k].count('(') == analisys[k].count(')'):
        resposta = 1
    else:
        resposta = 0
    respostas7.append(resposta)
for k in range(7, len(analisys), 10):
    if analisys[k].count('[') == analisys[k].count(']'):
        resposta = 1
    else:
        resposta = 0
    respostas8.append(resposta)
for k in range(8, len(analisys), 10):
    if analisys[k].count('{') == analisys[k].count('}'):
        resposta = 1
    else:
        resposta = 0
    respostas9.append(resposta)
for k in range(9, len(analisys), 10):
    if analisys[k].count('<') == analisys[k].count('>'):
        resposta = 1
    else:
        resposta = 0
    respostas10.append(resposta)
print(respostas1)
print(respostas2)
print(respostas3)
print(respostas4)
print(respostas5)
print(respostas6)
print(respostas7)
print(respostas8)
print(respostas9)
print(respostas10)
for k in range(0, len(respostas1)):
    if respostas1[k] == 1 and respostas2[k] == 1 and respostas3[k] == 1 and respostas4[k] == 1 and respostas5[k] == 1:
        solucao = 1
    if respostas6[k] == 1 and respostas7[k] == 1 and respostas8[k] == 1 and respostas9[k] == 1 and respostas10[k] == 1:
        solucao = 1
        solucoes.append(solucao)
    else:
        solucao = 0
        solucoes.append(solucao)
for k in range(0, len(solucoes)):
    print(solucoes[k], end=' ')


# reposta correta: 1 0 0 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 1 1
"""
import pandas as pd
import io

dados_raw = """Nome_Cliente	Logradouro	Bairro	Cidade	CEP	Codigo_Rastreamento
Renata Oliveira	Av. Paulista, 1136	Savassi	MG	28289-854	BR210053353BR
Eduardo Moreira	Rua Tiradentes, 2243	Centro	GO	65302-132	BR131994523BR
Mariana Pereira	Rua Bahia, 2079	Moema	SP	83563-303	BR868820204BR
Renata Nascimento	Rua Sete de Setembro, 1728	Savassi	DF	87236-384	BR969119330BR
Ana Santos	Av. Getúlio Vargas, 1741	Jardins	CE	30379-320	BR919795579BR
Camila Oliveira	Rua das Flores, 1566	Centro	RS	55082-718	BR384027113BR
Carlos Moreira	Av. Brasil, 2206	Centro	BA	20328-665	BR414797776BR
Renata Correia	Rua Tiradentes, 1491	Moema	MG	19116-146	BR810026086BR
Rafael Ribeiro	Rua das Flores, 963	Pinheiros	PR	59823-384	BR586845604BR
Renata Gomes	Av. Atlântica, 1526	Jardins	MG	97841-373	BR853573823BR
Eduardo Teixeira	Rua das Flores, 710	Aldeota	MG	31417-573	BR507437181BR
Juliana Teixeira	Av. Getúlio Vargas, 2291	Savassi	RS	17331-334	BR982403818BR
Carlos Carvalho	Rua São João, 1106	Centro	MG	84341-997	BR870854579BR
Camila Pereira	Rua Amazonas, 2054	Botafogo	DF	28726-371	BR249926919BR
Rafael Moreira	Rua Sete de Setembro, 2217	Meireles	GO	66155-697	BR528853029BR
Rodrigo Ferreira	Av. Atlântica, 2097	Lourdes	PR	16175-981	BR217734861BR
Beatriz Teixeira	Av. Atlântica, 1739	Moema	PR	60432-490	BR739830322BR
Aline Melo	Av. Beira Mar, 2276	Pinheiros	SP	99166-838	BR222998994BR
Eduardo Castro	Rua XV de Novembro, 1102	Batel	RS	24621-400	BR566825638BR
Gabriel Araujo	Av. Paulista, 1088	Aldeota	RJ	76542-208	BR771410971BR
Matheus Teixeira	Rua Sete de Setembro, 824	Copacabana	RS	31174-652	BR936043811BR
Leticia Silva	Av. Rio Branco, 1337	Lourdes	SP	24662-471	BR992994062BR
Matheus Ferreira	Av. Paulista, 996	Tijuca	GO	20322-187	BR885879795BR
Felipe Costa	Rua XV de Novembro, 2191	Batel	RJ	26828-775	BR610330567BR
Thiago Santos	Av. Beira Mar, 2171	Pinheiros	GO	65461-316	BR679064766BR
Amanda Moreira	Av. Getúlio Vargas, 833	Castelo	CE	62296-787	BR797801251BR
Rodrigo Araujo	Rua Tiradentes, 2129	Lourdes	PR	42493-330	BR168747287BR
Camila Silva	Av. Rio Branco, 2278	Savassi	GO	38864-107	BR176228245BR
Larissa Teixeira	Av. Paulista, 947	Centro	SP	53309-172	BR652070932BR
Rafael Almeida	Rua Amazonas, 1998	Savassi	PE	27342-840	BR713152854BR
Vanessa Barbosa	Rua Bahia, 1947	Batel	BA	34957-196	BR204078666BR
Eduardo Lima	Rua das Palmeiras, 1744	Botafogo	DF	17100-789	BR801642483BR
Carlos Martins	Av. Getúlio Vargas, 1399	Batel	PR	42591-296	BR304235259BR
Thiago Araujo	Av. Atlântica, 1738	Copacabana	CE	70637-355	BR180943908BR
Aline Castro	Rua das Flores, 217	Ipanema	PE	11934-195	BR909134796BR
Rafael Santos	Rua São João, 1999	Lourdes	MG	62565-160	BR276777762BR
Patricia Silva	Rua São João, 1096	Tijuca	DF	47388-533	BR847959430BR
Gustavo Castro	Rua Amazonas, 2003	Copacabana	MG	48890-322	BR162795957BR
Vanessa Moreira	Rua Sete de Setembro, 259	Castelo	RS	17492-151	BR727255918BR
Felipe Melo	Rua Tiradentes, 2185	Copacabana	SP	76562-182	BR299528037BR
Mariana Correia	Rua das Flores, 973	Botafogo	PR	84668-352	BR721609600BR
Diego Souza	Av. Rio Branco, 345	Botafogo	GO	84085-635	BR439699535BR
Juliana Pereira	Rua Amazonas, 1296	Savassi	CE	61876-234	BR821221887BR
Renata Ribeiro	Av. Brasil, 1305	Tijuca	PR	11220-569	BR766964667BR
Vanessa Oliveira	Rua das Flores, 2212	Savassi	PE	44760-235	BR474745382BR
Mariana Ferreira	Rua das Palmeiras, 1177	Copacabana	DF	81200-820	BR424825305BR
Diego Teixeira	Rua Sete de Setembro, 42	Ipanema	PE	49240-779	BR211225158BR
Beatriz Almeida	Rua das Flores, 448	Castelo	PE	30374-378	BR402533494BR
Diego Pereira	Av. Getúlio Vargas, 1414	Savassi	CE	76244-600	BR369639388BR
Carlos Costa	Rua Amazonas, 1744	Pinheiros	CE	15778-103	BR458153605BR
Amanda Rocha	Rua Amazonas, 1082	Copacabana	DF	82309-822	BR559225330BR
Thiago Silva	Rua das Flores, 318	Tijuca	RJ	81511-136	BR996139578BR
Rodrigo Cardoso	Rua Sete de Setembro, 616	Botafogo	RJ	15482-415	BR491541578BR
Carlos Gomes	Rua Bahia, 1032	Ipanema	PR	56357-898	BR701170349BR
Bruno Correia	Av. Getúlio Vargas, 643	Tijuca	MG	31299-919	BR970559510BR
Gabriel Lima	Av. Paulista, 744	Castelo	RS	63964-921	BR819307302BR
Gustavo Ferreira	Av. Beira Mar, 662	Batel	PR	60140-993	BR141580226BR
Felipe Ferreira	Rua Bahia, 1895	Jardins	CE	39831-328	BR125409494BR
Eduardo Pereira	Rua São João, 1354	Meireles	PR	46585-459	BR788785773BR
Leticia Martins	Rua Amazonas, 2206	Jardins	SP	25118-998	BR380477683BR
Gabriel Cardoso	Av. Beira Mar, 166	Centro	GO	66959-453	BR882269302BR
Camila Lima	Av. Rio Branco, 2104	Centro	BA	85574-294	BR373506211BR
Carlos Nascimento	Rua São João, 16	Aldeota	PE	97900-301	BR491079829BR
Bruno Costa	Rua Amazonas, 1362	Moema	RS	96951-968	BR233815413BR
Gustavo Ribeiro	Rua Sete de Setembro, 1276	Ipanema	BA	52753-512	BR848621833BR
Matheus Castro	Av. Atlântica, 795	Botafogo	BA	98777-866	BR286860433BR
Diego Cardoso	Av. Beira Mar, 1673	Aldeota	SP	49829-393	BR325681936BR
Bruno Cardoso	Av. Rio Branco, 1329	Lourdes	DF	67954-791	BR329460134BR
Leticia Barbosa	Rua XV de Novembro, 705	Ipanema	PR	47196-627	BR812807629BR
Camila Costa	Av. Independência, 972	Ipanema	CE	39444-925	BR313814138BR
Beatriz Silva	Av. Paulista, 1012	Lourdes	GO	19545-566	BR545002643BR
Renata Cardoso	Rua Bahia, 1582	Lourdes	BA	41979-251	BR804436922BR
Larissa Silva	Rua Tiradentes, 446	Batel	BA	38683-280	BR963406382BR
Larissa Melo	Av. Brasil, 215	Aldeota	MG	25906-567	BR243171768BR
Aline Borges	Rua Sete de Setembro, 2299	Moema	RS	68008-727	BR975106572BR
Gustavo Melo	Rua São João, 2254	Lourdes	RJ	72216-560	BR378304807BR
Amanda Ferreira	Av. Independência, 1145	Batel	PE	73517-741	BR356888294BR
Juliana Araujo	Rua das Flores, 1180	Savassi	CE	54020-427	BR679984033BR
Mariana Rocha	Av. Atlântica, 957	Botafogo	RJ	38043-165	BR545461013BR
Bruno Carvalho	Rua Sete de Setembro, 1918	Botafogo	SP	37110-952	BR551125671BR
Patricia Cardoso	Av. Getúlio Vargas, 90	Pinheiros	GO	59857-588	BR106330865BR
Rodrigo Ribeiro	Rua XV de Novembro, 1607	Pinheiros	BA	80545-865	BR888807316BR
Thiago Correia	Rua Tiradentes, 913	Lourdes	MG	45774-546	BR621454127BR
Ana Martins	Rua das Palmeiras, 1666	Castelo	RJ	71261-230	BR768143326BR
Vanessa Borges	Av. Paulista, 353	Ipanema	BA	27786-987	BR595744935BR
Gabriel Souza	Av. Beira Mar, 1562	Jardins	MG	69598-434	BR462388455BR
Amanda Martins	Av. Beira Mar, 1736	Meireles	PR	71644-119	BR904258674BR
Thiago Souza	Rua das Palmeiras, 928	Ipanema	PR	95426-141	BR909851739BR
Ana Ferreira	Rua Bahia, 93	Moema	RJ	41266-229	BR608482316BR
Eduardo Oliveira	Av. Rio Branco, 902	Lourdes	CE	58351-271	BR750572325BR
Diego Moreira	Av. Getúlio Vargas, 479	Batel	RJ	50768-210	BR721358005BR
Ana Ribeiro	Av. Rio Branco, 1547	Botafogo	MG	19961-706	BR841541582BR
Renata Ferreira	Rua das Flores, 1245	Pinheiros	GO	25866-915	BR707665448BR
Thiago Lima	Rua Amazonas, 1527	Centro	PE	94874-449	BR113585139BR
Bruno Barbosa	Rua das Flores, 1785	Jardins	DF	30052-545	BR289125618BR
Renata Almeida	Av. Rio Branco, 2214	Batel	DF	70931-546	BR986625773BR
Gustavo Cardoso	Av. Beira Mar, 1330	Pinheiros	MG	21359-385	BR584044963BR
Rafael Araujo	Av. Rio Branco, 1562	Jardins	SP	74789-971	BR448981305BR
Gabriel Barbosa	Rua Bahia, 1463	Batel	CE	54608-386	BR740116562BR
Larissa Almeida	Rua Sete de Setembro, 51	Aldeota	MG	21221-347	BR873174285BR"""

df = pd.read_csv(io.StringIO(dados_raw), sep='\t', dtype=str)
df.to_excel("Envios.xlsx", index=False, engine="openpyxl")

print("Sucesso! O arquivo Envios.xlsx com 100 registros foi gerado na sua pasta.")
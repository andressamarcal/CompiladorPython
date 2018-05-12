#				COMPYLA				 

-------------------------------------------------------------------------------------------------------


> Classes do Projeto
       Foram modeladas classes que ao mesmo tempo podesse ser autoexplicativas e mais próximas possíveis das
	entidades envolvidas em uma analisador lexico e sintático.
		Fica assim o trabalho resumido as classes:
			1. Principal 
			2. AnalisadorLexico 
			3. AnalisadorSintatico 

       Vejamos um pouco sobre cada uma delas abaixo e sua ação no projeto:
           
	   1. Principal.py
               A classe principal está exclusivamente ligada ao processo de execução do analisador, ela exerce a
				mesma função que teria o compilador: levantar os tokens e processar sua analise sintática;
    	2. AnalisadorLexico.py
               Funciona com as mesmas funções que se espera de um analisador Léxico. Faz a abertura do arquivo passado
				como parâmetro, faz a remoção de comentários, conta o número de linhas, conta o número de caracteres e
			e faz o levantamento de tokens nos arquivo;
        3. AnalisadorSintatico.py
               A partir do levantamento feito pelo analisador Léxico, o analisador sintático é capaz se a estruturação
				do arquivo é correta e atende a linguagem definida 

------------------------------------------------------------------------------------------------------

# Como Rodar:


*Comando > python2 Principal.py [nomedoarquivoteste].txt

*A saída do programa se resume a apenas duas possibilidades:*
			**true**  - Caso a análise sintática e léxica esteja correta e dentro do esperado 
			**false** - Caso exista algum erro léxico, sintático ou de outra origem 

	
	para maiores informações sobre como foi realizado a execução e se houve alguma ocorrência, o programa produz um
	*arquivo de log* que tem o nome *[ANO-MES-DIA].log*
	ele está dividido por sessões, ou seja, por execução do
	programa.


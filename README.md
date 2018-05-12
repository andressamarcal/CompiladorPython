#				COMPYLA				 

------------------------------------------------------------------------------------------------


### Classes do Projeto

1. Principal.py 

A classe principal está ligada ao processo de execução do analisador, ela exerce a mesma função que teria o compilador: levantar os tokens e processar sua analise sintática;

2. AnalisadorLexico.py

Faz a abertura do arquivo passado como parâmetro, faz a remoção de comentários, conta o número de linhas, conta o número de caracteres e faz o levantamento de tokens nos arquivo;

3. AnalisadorSintatico.py 
 
O analisador sintático vê se a estruturação do arquivo é correta e atende a linguagem definida;

------------------------------------------------------------------------------------------------

### Rodando o programa:


*Comando* 
> $ python2 Principal.py teste/[nomedoarquivodeteste].txt

*A saída do programa se resume a apenas duas possibilidades:*
			
			*true*  - Caso a análise sintática e léxica esteja correta e dentro do esperado 
			
			*false* - Caso exista algum erro léxico, sintático ou de outra origem 

	
### Log:

Ao executar o programa, se houve alguma ocorrência, o programa produz um *arquivo de log* que tem o nome *[ANO-MES-DIA].log* ele está dividido por sessões, ou seja, por execução do programa.


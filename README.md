# Projeto de Software Refatorado
No projeto original, foram encontrados diversos **code smells** tais quais:
1. Duplicated Code  
2. Long parameter list
4. Long method
5. Dead code
6. Middle man
7. Long class
8. Switch Statements
9. Primitive Obsession

# Refactoring
Foram usados os seguinte padrões de design para refatoramento:
- **Strategy**: Para cada botão de submissão que é apertado, uma nova janela é criada, e ela depende de algumas checagens. Tais checagens têm a estrutura geral semelhante, mas são diferentes em seu fim. Desta forma, decidi implementar o padrão de design complexo Strategy, pois pude utilizar de conceitos de herança e polimorfismo para diminuir consideravelmente o número de linhas utilizado, além de melhorar a organização. 

- **Extract Method**: Com este padrão de design eu pude eliminar tanto os long methods quanto as long class. Pude também terceirizar grandes switch statements.

- **Extract Class**: Muitas linhas de código eram repetidas para criar-se botões e seus frames. Dessa forma, criei uma classe que terceiriza estas ações e usei o padrão de design Command para lidar com os requests dos botões. Lidei também com *Primitive Obsession* e com *Long Class* usando este padrão de design

- **Command**: Cada botão precisa executar um request único! Por isso, usei o padrão *Command* para organizar e simplificar o código do menu principal. 

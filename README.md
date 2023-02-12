# django_e-commerce
Projeto desenvolvido em python utilizando django simulando um e-commerce

Intruções:

- Projeto será manipulado pelo shell do django;
- Você deve utilizar o seguinte comando: "python manage.py shell".
- Depois devemos importa qual pasta e classes utilizadas com seguinte comando: "from nome_da_pasta.models import nome_da_classe, nome_da_classe";
- Logo em seguida podemos manipular essas classes utilizando o comando para iniciar as classes: "nome_do_objeto = nome_da_classe()";
- Para atribuir valores aos atributos utilizamos o seguinte comando: "nome_do_objeto = nome_da_classe.objects.set(nome_do_atributo="valor")";
- Para salvar no banco de dados esse produto utilizamos: "nome_do_objeto.save()";
- Para salvar no carrinho devemos inicializar o carrinho primeiro, utilizando: "nome_do_objeto = nome_da_classe()" sempre vai inicializar uma lista vazia para trabalhar com os itens do carrinho separados;
- Para incluir algum produto a lista do carrinho utilizamos o seguinte comando: "nome_do_objeto.adicionarAoCarrinho(nome_do_objeto_produto)";
- Para remover algum produto da lista do carrinho utilizamos o seguinte comando: "nome_do_objeto.removerDoCarrinho(nome_do_objeto_produto)";
- Para listar os itens do carrinho: "nome_do_objeto.listarProdutos()";
- Para calcular o valor geral dos produtos adicionados utilizamos: "nome_do_objeto.subTotal()";
- Para calcular o valor total dos produtos com frete incluso: "nome_do_objeto.valorTotalCarrinho()";
- Você também pode ordenar os produtos do carrinho pela descrição utilizando: "nome_do_objeto.orderByDescription()";
- Para ordenar pelo valor dos produtos, utilizamos: "nome_do_objeto.orderByValue()";
- Para finalizar sua compra você pode finalizar utilizando: "nome_do_objeto.comprar()" assim você receberá uma mensagem de confimação e seu carrinho será limpado automaticamente.

# dj-Gentella

Django integrado con plantilla Gentella.

# 16/03/2022

Creacion de modelos y su respecto CRUD para los modelos:

- Categoria
- SubCategoria
- Marca
- Unidad de Medida
- Producto
- User (solo ingresa con correo electronico)

(Observaciones):

- Los objetos no pueden ser borrados solo inactivados, con un solo View..
- Todo el CRUD de los modelos esta basada en Views heredadas de 'core/views.py'.
- La autenticacion esta realizandose a travez de los correos (Login, Logout, CreateUser).
- Intregracion de Easy Thumbnail para la genereacion de miniaturas.

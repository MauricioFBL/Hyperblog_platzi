@REM  inicializar git
git init 
@REM Estatus del proyecto
git status   
@REM Añadir archivos para ser enviados
git add archivo.algo
@REM Sacar de envio 
git rm archivo.algo
@REM quitar de memoria ram
git rm --cached archivo.algo
@REM Configuracion de usuario
git config --global user.name "Mauricio Bautista"
git config --global user.email Mauricio.Bautista@dentsu.com
@REM listar Configuracion
git config --list
@REM Añadir todos los archivos de una carpeta
git add .
@REM Subir completamente archivos de carpeta
git commit -m ""
git status
@REM ver historial de cambios de un archivo
git log archivo.algo
@REM muestra diferencia entre version anterior y version nueva
git show .\algo.txt
@REM ESC SHIFT ZZ
git commit
@REM comparar contenido de acuerdo indices de comit
git diff 07c6676d979928f924dc284f35f3f51f33e1a804 ee2fc3536aa3b4bc267f3155423ac202d72d386e
@REM git diff archivo indicecomitcomparar indicecomparador
@REM EXISTEN 3 AREAS DIFERENTES EN git
@REM UNTRACKED AREA (Working directory)
@REM git no sabe que existe

@REM STAGGING AREA - AREA EN MEMORIA RAM  DESCONECTADA DE TODO
git add
@REM  Repositorio (master)
@REM  Donde se llega la ultima version
git commit
git checkout 
@REM __________________________________________________________________
@REM REINCIAR COMPLETAMENTA VERSION ELEGIDA DE COMMIT
@REM elimina todo el historia de commita
git reset id_cambio --hard
@REM __________________________________________________________________
git reset id_cambio --soft
@REM mostrar cambios de todos los archivos
git diff
@REM ver el cambios especificos de cada archio
git log --stat
@REM Regresar auna version del archivo sin cambiar en master
git checkout indice_commit archivo.algo
@REM Regresar a master despues de un checkout sin commit
git checkout master archivo.algo


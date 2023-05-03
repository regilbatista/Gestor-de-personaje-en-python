from funciones import *

seguimos = True

while seguimos:
    lim()
    print(""" 
                                                                                               
                                                                                                         
    ,---,. ,--,           ,-.----.                                                                ____   
  ,'  .' ,--.'|           \    /  \                     ,--,  ,-.----.                          ,'  , `. 
,---.'   |  | :           ;   :    \               .--,--.'|  \    /  \  __  ,-.  ,---.      ,-+-,.' _ | 
|   |   .:  : '           |   | .\ :             .--,`|  |,   |   :    ,' ,'/ /| '   ,'\  ,-+-. ;   , || 
:   :  |-|  ' |           .   : |: |   ,---.     |  |.`--'_   |   | .\ '  | |' |/   /   |,--.'|'   |  || 
:   |  ;/'  | |           |   |  \ :  /     \    '--`_,' ,'|  .   : |: |  |   ,.   ; ,. |   |  ,', |  |, 
|   :   .|  | :           |   : .  / /    /  |   ,--,''  | |  |   |  \ '  :  / '   | |: |   | /  | |--'  
|   |  |-'  : |__         ;   | |  \.    ' / |   |  | |  | :  |   : .  |  | '  '   | .; |   : |  | ,     
'   :  ;/|  | '.'|        |   | ;\  '   ;   /|   :  | '  : |__:     |`-;  : |  |   :    |   : |  |/      
|   |    ;  :    ;        :   ' | \.'   |  / | __|  : |  | '.':   : :  |  , ;   \   \  /|   | |`-'       
|   :   .|  ,   /         :   : :-' |   :    .'__/\_: ;  :    |   | :   ---'     `----' |   ;/           
|   | ,'  ---`-'          |   |.'    \   \  /|   :    |  ,   /`---'.|                   '---'            
`----'                    `---'       `----'  \   \  / ---`-'   `---`                                    
                                               `--`-'        
    Elija una opcion              
        1- Gestionar Personajes.
        2- Reportes 
        3- Configuración 
        4- Acerca De
        5- Salir 
 
     """)

    opcion = input("Seleccione una opcion: ")

    if opcion == '1':
               co = True
               while co:
                  print("""
                Elija una opcion              
                  1- Agregar
                  2- Modificar 
                  3- Eliminar
                  4- Regresar 
                  """)
                  opc = input("Seleccione una opcion: ")
                  if opc =='1':
                     agper()
                  elif opc == '2':
                     modper()
                  elif opc == '3':
                     elimper()
                  elif opc == '4':
                     co= False
                  else:
                   input('Elija una opcion valida del 1 al 4  ┗|｀O′|┛')

    elif opcion == '2':
      
               c = True
               while c:
                  print("""
                  Elija una opcion              
                  1- Listado de personajes
                  2- listado por signo zodiacal
                  3- Reporte de cumpleaños
                  4- Mapas de 
                  5- Exportar
                  6- Listado de personajes por serie
                  7- Listado de personajes por estado
                  8- Regresar 
                  """)
                  opci = input("Seleccione una opcion: ")
                  if opci =='1':
                    showlistper()
                  elif opci == '2':
                    showlistsigno()
                  elif opci == '3':
                     showlistedad()
                  elif opci == '4':
                     export()
                  elif opci == '5':
                     Export()
                  elif opci == '6':
                     showlistserie()
                  elif opci == '7':
                     showlistest()
                  elif opci== '8':
                     c= False
                  else:
                     input('Elija una opcion valida del 1 al 8  ┗|｀O′|┛')

    elif opcion == '3':
               co = True
               while co:
                  print("""
                Elija una opcion              
                  1- Serie
                  2- Estados
                  3- Sexo
                  4- Regresar 
                  """)
                  opc = input("Seleccione una opcion: ")
                  if opc =='1':
                         cor = True
                         while cor:
                            print("""
                            Elija una opcion              
                            1- Agregar
                            2- Modificar 
                            3- Eliminar
                            4- Regresar 
                            """)
                            opc = input("Seleccione una opcion: ")
                            if opc =='1':
                                agser()
                            elif opc == '2':
                                modser()
                            elif opc == '3':
                                elimser()
                            elif opc == '4':
                                cor= False
                            else:
                              input('Elija una opcion valida del 1 al 4  ┗|｀O′|┛')
                  elif opc == '2':
                         cor = True
                         while cor:
                            print("""
                            Elija una opcion              
                            1- Agregar
                            2- Modificar 
                            3- Eliminar
                            4- Regresar 
                            """)
                            opc = input("Seleccione una opcion: ")
                            if opc =='1':
                                agest()
                            elif opc == '2':
                                modest()
                            elif opc == '3':
                                elimest()
                            elif opc == '4':
                                cor= False
                            else:
                              input('Elija una opcion valida del 1 al 4  ┗|｀O′|┛')
                    
                  elif opc == '3':
                         cor = True
                         while cor:

                            print("""
                            Elija una opcion              
                            1- Agregar
                            2- Modificar 
                            3- Eliminar
                            4- Regresar 
                            """)
                            opc = input("Seleccione una opcion: ")
                            if opc =='1':
                                agsex()
                            elif opc == '2':
                                modsex()
                            elif opc == '3':
                                elimsex()
                            elif opc == '4':
                                cor= False
                            else:
                              input('Elija una opcion valida del 1 al 4  ┗|｀O′|┛')
                  elif opc == '4':
                     co= False
                  else:
                   input('Elija una opcion valida del 1 al 4  ┗|｀O′|┛')
    elif opcion == '4':

        print("Habriendo youtube...")
        aboutme()
        
    elif opcion == '5':
      
        seguimos = False
  
       
        input("Presione enter para cerra el programa")
    else:
     input('Elija una opcion valida del 1 al 4  ┗|｀O′|┛')

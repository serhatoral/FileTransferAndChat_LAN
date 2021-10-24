from random import randint
from rich.console import Console


class AsciiArt:

    consol = Console()
    arts =[ """[bold green]\

                                       ._ o o
                                       \_`-)|_
                                    ,""       \ 
                                  ,"  ## |   ಠ ಠ. 
                                ," ##   ,-\__    `.
                              ,"       /     `--._;)
                            ,"     ## /
                          ,"   ##    /

                    [/]""",

        """[bold yellow]

         ______________
        /             /|
       /             / |
      /____________ /  | 
     | ___________ |   |
     ||           ||   |
     ||           ||   |
     ||           ||   |
     ||___________||   |
     |   _______   |  /
    /|  (_______)  | /
   ( |_____________|/
   (
.=======================.
| ::::::::::::::::  ::: |
| ::::::::::::::[]  ::: |
|   -----------     ::: |
`-----------------------'  
                        
 [/]""",


""" [red]

                   ,,,, 
             ,;) .';;;;',
 ;;,,_,-.-.,;;'_,|I\;;;/),,_
  `';;/:|:);{ ;;;|| \;/ /;;;\__
      L;/-';/ \;;\',/;\/;;;.') :
      .:`''` - \;;'.__/;;;/  . _'-._ 
    .'/   \     \;;;;;;/.'_7:.  '). \_
  .''/     | '._ );}{;//.'    '-:  '.,L
.'. /       \  ( |;;;/_/         \._./;\   _,
 . /        |\ ( /;;/_/             ';;;\,;;_,
. /         )__(/;;/_/                (;;'''''
 /        _;:':;;;;:';-._             );
/        /   \  `'`   --.'-._         \/
       .'     '.  ,'         '-,
      /    /   r--,..__       '.;
    .'    '  .'        '--._     ]
    (     :.(;>        _ .' '- ;/
    |      /:;(    ,_.';(   __.'
     '- -'"|;:/    (;;;;-'--'
           |;/      ;;(
           ''      /;;|
                   \;;|
                    \/


[/] """,

"""[cyan]

     _.._   _..---.,
  .-"    ;-"        }
 /      /           |
|      |       _=   |
;   _.-'\__.-')     |
 `-'      |   |    ;
          |  /;   /      _,
        .-.;.-=-./-""-.-` _`
       /   |     \     \-` `,
      |    |      |     |
      |____|______|     |
       \ 0 / \  0 /     /
    .--.-""-.`--'     .'
   (#   )          ,  \.
   ('--'          /\`  \.
    \       ,,  .'      \.
     `-._    _.'\        \.
         `""`    \        \.


[/]""",



"""[white]

           _                         _
       _==/          i     i          \==
     /XX/            |\___/|            \XX;
   /XXXX\            |XXXXX|            /XXXX;
  |XXXXXX\_         _XXXXXXX_         _/XXXXXX|
 XXXXXXXXXXXxxxxxxxXXXXXXXXXXXxxxxxxxXXXXXXXXXXX
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|
 XXXXXX/^^^^"\XXXXXXXXXXXXXXXXXXXXX/^^^^^\XXXXXX
  |XXX|       \XXX/^^\XXXXX/^^\XXX/       |XXX|
    \XX\       \X/    \XXX/    \X/       /XX/
       "\       "      \X/      "       /"
                        !


""",

"""[blue]

         __
 _(\    |@@|
(__/\__ \--/ __
   \___|----|  |   __
       \ }{ /\ )_ / _)
       /\__/\ \__O (__
      (--/\--)    \__/
      _)(  )(_
     `---''---`


""",

"""[green]

                 ___====-_  _-====___
           _--^^^#####//      \\#####^^^--_
        _-^##########// (    ) \\##########^-_
       -############//  |\^^/|  \\############-
     _/############//   (@::@)   \\############\_
    /#############((     \()/     ))#############;
   -###############(\    (oo)    //###############-
  -#################(\  / VV \  //#################-
 -###################(\/      \//###################-
_#/|##########/\######(   /\   )######/\##########|\#_
|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
   `   `  `      `   / | |  | | \   '      '  '   '
                    (  | |  | |  )
                   __\ | |  | | /__
                  (vvv(VVV)(VVV)vvv)


""",

"""[red]

        _____,    _..-=-=-=-=-====--,
     _.'a   /  .-',___,..=--=--==-'`
    ( _     \ /  //___/-=---=----'
     ` `\    /  //---/--==----=-'
  ,-.    | / \_//-_.'==-==---='
 (.-.`\  | |'../-'=-=-=-=--'
  (' `\`\| //_|-\.`;-~````~,        _
       \ | \_,_,_\.'        \     .'_`;
        `\            ,    , \    || `\?
          \    /   _.--\    \ '._.'/  / |
          /  /`---'   \ \   |`'---'   \/
         / /'          \ ;-. ;
      __/ /           __) \ ) `|
    ((='--;)         (,___/(,_/



[/]""",


"""

              ,,))))))));,
           __)))))))))))))),
\|/       -\(((((''''((((((((.
-*-==//////((''  .     `)))))),
/|\      ))| o    ;-.    '(((((                                  ,(,
         ( `|    /  )    ;))))'                               ,_))^;(~
            |   |   |   ,))((((_     _____------~~~-.        %,;(;(>';'~
            o_);   ;    )))(((` ~---~  `::           \      *%~~)(v;(`('~
                  ;    ''''````         `:       `:::|\,__,;%    );`'; ~
                 |   _                )     /      `:|`----'     `-'
           ______/\/~    |                 /        /
         /~;;.____/;;'  /          ___--,-(   `;;;/
        / //  _;______;'------~~~~~    /;;/\    /
       //  | |                        / ;   \;;,)
      (<_  | ;                      /',/-----'  _>
       \_| ||_                     //~;~~~~~~~~~
           `\_|                   (,~~  
                                   \~;
                                    ~~


""",


"""[yellow]

    XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
 XXXXXXXXXXXXXXXXXX         XXXXXXXX
XXXXXXXXXXXXXXXX              XXXXXXX
XXXXXXXXXXXXX                   XXXXX
 XXX     _________ _________     XXX      
  XX    I  _xxxxx I xxxxx_  I    XX        
 ( X----I         I         I----X )          
( +I    I      00 I 00      I    I+ )
 ( I    I    __0  I  0__    I    I )
  (I    I______ /   \_______I    I)
   I           ( ___ )           I
   I    _  :::::::::::::::  _    i
    \    \___ ::::::::: ___/    /
     \_      \_________/      _/
       \        \___,        /
         \                 /
          |\             /|
          |  \_________/  |



[/]"""




 ]



    def random_art(self):
        index =  randint(0,9)
        self.consol.print(self.arts[index])


 
 
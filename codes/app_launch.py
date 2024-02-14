#####
#Script de lancement de l'application
####
import sys
sys.path.append('codes/UI/')
import Navigation
sys.path.append('dataBases/')
import Raw_database_traitements

launch = input("First time on the app ? (1/0) : ")

if launch :
    Raw_database_traitements.normalise_data_base()

Navigation.main()
    
from core.auth.ressource import *

##################################################################
######################## PERMISSIONS #############################
##################################################################
#                                                                #
#   FICHIER LISTANT L'ENSEMBLE DES PERMISSIONS ET ACTIONS SUR    #
#                 LES RESSOURCES DE L"APPLICATON                 #
#                                                                #
##################################################################
######################## PERMISSIONS #############################
##################################################################


# CATEGORY PERMISSIONS
ADD_CATEGORY = CATEGORY.add
VIEW_CATEGORY = CATEGORY.view
CHANGE_CATEGORY = CATEGORY.change
DELETE_CATEGORY = CATEGORY.delete



# PRODUCT PERMISSIONS
ADD_PRODUCT = PRODUCT.add
VIEW_PRODUCT = PRODUCT.view
CHANGE_PRODUCT = PRODUCT.change
DELETE_PRODUCT = PRODUCT.delete
ARCHIVE_PRODUCT = PRODUCT.archive



# SALE PERMISSIONS
ADD_SALE = SALE.add
VIEW_SALE = SALE.view
CHANGE_SALE = SALE.change
DELETE_SALE = SALE.delete
REFUND_SALE = SALE.refund
EXPORT_SALE = SALE.export



# CUSTOMER PERMISSIONS
ADD_CUSTOMER = CUSTOMER.add
VIEW_CUSTOMER = CUSTOMER.view
CHANGE_CUSTOMER = CUSTOMER.change
DELETE_CUSTOMER = CUSTOMER.delete


# USER PERMISSIONS
ADD_USER = USER.add
VIEW_USER = USER.view
CHANGE_USER = USER.change
DELETE_USER = USER.delete
BLOCK_USER = USER.block

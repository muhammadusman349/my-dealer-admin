Company_permission_choices = [
                    ('can_view_role','can view role'),
                    ('can_add_role','can add role'),
                    ('can_update_role','can update role'),
                    ('can_delete_role','can delete role'),

                    ('can_view_admin_member','can view admin member'),
                    ('can_add_admin_member','can add admin member'),
                    ('can_update_admin_member','can update admin_member'),
                    ('can_delete_admin_member','can delete admin member'),
                    ]

Sales_representative_choices = [
                    ('can_view_role','can view role'),
                    ('can_add_role','can add role'),
                    ('can_update_role','can update role'),
                    ('can_delete_role','can delete role'),

                    ('can_view_Sr_member','can view Sr member'),
                    ('can_add_Sr_member','can add Sr member'),
                    ('can_update_Sr_member','can update Sr member'),
                    ('can_delete_Sr_member','can delete Sr member'),

]


Dealer_choices = [
                    ('can_view_role','can view role'),
                    ('can_add_role','can add role'),
                    ('can_update_role','can update role'),
                    ('can_delete_role','can delete role'),

                    ('can_view_Dealer_member','can view Dealer member'),
                    ('can_add_Dealer_member','can add Dealer member'),
                    ('can_update_Dealer_member','can update Dealer member'),
                    ('can_delete_Dealer_member','can delete Dealer member'),

]


user_choices=[('admin',"Admin"),('dealer','Dealer'),('repair_facility','Repair Facility'),('sales_representative','Sales Representative'),('agency','Agency')]

producer_type = [('franchise','Franchise'),('independent','Independent'),('bank','Bank'),('credit union','Credit Union')]

claim_review_choices = [('oem','OEM'),('after market','After Market')]

payment_method_choices = [('stripe','Stripe'),('dwolla','Dwolla')]
 
dealer_of = [('admin','Admin'),('agency','Agency')]
def get_customer_invoices_paid(request, id):
#     customer = Customer.objects.get(id=id)
#     customer_invoices = customer.sender.filter(status="CP")
#     return render(request, 'customers.html', {"customer_invoices": customer_invoices})
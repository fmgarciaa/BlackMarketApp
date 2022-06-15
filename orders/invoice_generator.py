import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, cm
from .models import Order, OrderItem
from customers.models import Customers
from products.models import Product

    
def some_view(request, id):

    data_customer = get_customer_data(id)
    data_items = get_items_order(id)
    
    business_details = (
        u"Naty's Juane",
        u"Facebook: Naty's Juane",
        u'Instagram: @natysjuane',
        u'WhastApp: 957 906 764'
    )
    buffer = io.BytesIO()
    pagesize = (57 * mm, 228 * mm)
    p = canvas.Canvas(buffer, pagesize=pagesize)
    h_header = 85
    v_header =630

    #DRAW HEADER
    for i in range(0, len(business_details)):
        if i == 0:
            p.setFont("Helvetica-Bold",9)
        else:
            p.setFont("Helvetica",8)

        p.drawCentredString(h_header , v_header, business_details[i])
        v_header-=10

    p.drawRightString(155,585, '================================')
    
    # DRAW CUSTOMER INFO
    p.drawCentredString(h_header, 575, "B001-"+str(id))
    h_customer=10
    
    p.drawString(h_customer, 565, "Nombre: "+data_customer['name'])
    p.drawString(h_customer, 555, "Celular: "+data_customer['phone'])
    p.drawString(h_customer, 545, "Direccion: "+data_customer['direction'])
    p.drawString(h_customer, 535, "Distrito: "+data_customer['distric'])
    p.drawString(h_customer, 525, "Referencia: "+data_customer['reference'])
    p.drawRightString(155,510, '================================')  

    # DRAW ORDER ITEMS
    h_items = 5
    v_items = 495
    p.drawString(h_items, v_items, 'Producto')
    p.drawString(h_items+40, v_items, 'Cantidad')
    p.drawString(h_items+80, v_items, 'P.Unit')
    p.drawString(h_items+110, v_items, 'SUBTOTAL')
    p.drawString(h_items, v_items-10, '---------------------------------------------------------')
    total_order=0
    v_items2 = 475
    for key, value in data_items.items():
        p.drawString(h_items, v_items2,value['product'])
        p.drawString(h_items+50, v_items2-10,str(value['quantity']))
        p.drawString(h_items+80, v_items2-10,str(value['price']))
        p.drawString(h_items+130, v_items2-10,str(value['total_item']))
        total_order+=value['total_item']
        v_items2-=20

    gravada = float(total_order)/1.18
    igv = gravada*0.18
    p.drawString(h_items, v_items2, '---------------------------------------------------------')  
    p.drawRightString(h_items+100, v_items2-10, 'OP.NOGRAVADA' )
    p.drawRightString(h_items+110, v_items2-10, 'S/' )
    p.drawString(h_items+130, v_items2-10, str(round(gravada,2)))

    p.drawRightString(h_items+100, v_items2-20, 'IGV' )
    p.drawRightString(h_items+110, v_items2-20, 'S/' )
    p.drawString(h_items+130, v_items2-20, str(round(igv,2)))

    p.setFont("Times-Bold",10)
    p.drawRightString(h_items+100, v_items2-30, 'TOTAL' )
    p.drawRightString(h_items+110, v_items2-30, 'S/' )
    p.drawString(h_items+125, v_items2-30, str(total_order))
    # DRWA FOOT
    p.drawString(h_items+10, v_items2-70, '*** Gracias por su compra ***')
    p.showPage()
    p.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=f'ticket{id}.pdf')


def get_customer_data(id):
    query_order = Order.objects.filter(id=id).values_list()
    id_customer = query_order[0][1]
    query_customer = Customers.objects.filter(id=id_customer).values_list()
    customer_data = {
        'name' : query_customer[0][1],
        'phone' : query_customer[0][2],
        'direction' : query_customer[0][3],
        'distric' : query_customer[0][4],
        'reference' : query_customer[0][5]
    }
    return customer_data


def get_items_order(id):
    query_order_item = OrderItem.objects.filter(order=id).values_list()
    items = {}
    key_item = 0
    for item in query_order_item:
        name_item = Product.objects.filter(id=item[2]).values()
        items[key_item] = {
            'product': name_item[0]['name'],
            'price' : item[4],
            'quantity' : item[3],
            'total_item': item[3]*item[4]
        }
        key_item +=1
    return items

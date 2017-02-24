from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from braces.views import GroupRequiredMixin,SuperuserRequiredMixin,LoginRequiredMixin
from django.views.generic import TemplateView
# from barcode import generate
from students.models import Child_detail
# import xhtml2pdf.pisa as pisa
# import cStringIO as StringIO
# from django.template.loader import get_template
# from django.template import Context
from django.conf import settings
import os.path
from django.http import HttpResponse, Http404



def render_to_pdf(template_src, context_dict,filename):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, link_callback=fetch_resources)
    if not pdf.err:
        outfile = HttpResponse(result.getvalue(), mimetype="application/pdf")
        outfile['Content-Disposition'] = 'attachment; filename='+filename+'.pdf'
        return outfile
    return http.HttpResponse('We had some error on report generation<pre>%s</pre>' % cgi.escape(html))

def fetch_resources(uri,rel):
    path=os.path.join(settings.MEDIA_ROOT,uri.replace(settings.MEDIA_URL,""))
    return path

def barcode_generator(request,uid):
    if request.POST:
        uid=request.POST.get('uuid')
    if uid:
        try:
            child= Child_detail.objects.get(unique_id_no=uid)
            img = child.photograph
            img_name = str(img).replace(".jpg",".125x125.jpg")
            student_barcode = generate('EAN13', uid, output='%s/%s' %(settings.MEDIA_ROOT,uid))
            return render(request,'students/id_card/id_card.html',{'child':child, 'student_barcode':student_barcode,'img_name':img_name})
        except:
            
            return render(request,'students/id_card/id_card.html',{'error': "Invalid UID. Please try again"})
        
    else:
        return render(request,'students/id_card/id_card.html')










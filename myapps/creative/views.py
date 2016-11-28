from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from myapps.creative.models import CreativeZhibo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt ##包装csrf请求，避免django认为其实跨站攻击脚本
from myapps.creative.editadd import add_edit
from myapps.report.paginator import list_page
from django.contrib.auth.decorators import login_required
import os
import time
# Create your views here.

class CreativePageView(ListView):
    ''' 展示素材中心首页的数据，并对数据进行分页'''
    @login_required
    def list_view(request):
        zhibo_list = CreativeZhibo.objects.filter(is_delete=0).order_by('-create_time') # 把没有删除的数据按照时间顺序展示出来
        '''这个是为了搜索框里是否有关键字，如果搜索框有值传过来的话，就根据值查出相匹配的，目前只以素材名称为匹配条件'''
        if request.method == 'GET':
            keyword = request.GET.get('keyword', '')
            zhibo_list = zhibo_list.filter(name__contains=keyword)

        # 分页代码
        '''备注：如果引用公共的分页方法，则原来展示数据的方法一定要改，例如前端原来展示数据是用
        {% for zhibo in zhibo_list %}取出的，现在则必须要用{% for zhibo in zhibo_list.list %}取出数据展示出来。因为
        公共的分页方法，数据是在list里面'''

        pagination = list_page(request,list=zhibo_list,display=10,after_range_num=3,bevor_range_num=2)
        getValue = '?keyword='+keyword

        '''
        # paginator = Paginator(zhibo_list, display_amount)
        # try:
        #     page = int(request.GET.get('page'))
        # except:
        #     page = 1
        # try:
        #     zhibo_list = paginator.page(page)
        # except PageNotAnInteger:
        #     zhibo_list = paginator.page(1)  # 页码不是整数,返回第一页
        # except EmptyPage:
        #     zhibo_list = paginator.page(paginator.num_pages)
        # if page > after_range_num:
        #     page_range = paginator.page_range[page - after_range_num:page + bevor_range_num]
        # else:
        #     page_range = paginator.page_range[0:page + bevor_range_num]
        '''
        content = {
            'active_menu' : '素材中心',
            'zhibo_list': pagination,
            # 'page_range': page_range,
            'query_category':getValue,
        }
        return render(request,'creative/materialCenter.html',content)

    #编辑素材
    '''当点击编辑素材的时候，把新编辑的素材内容重新赋值给原来数据库里的内容。而且重新打一个tar包'''
    @csrf_exempt
    def edit_view(request):
        if request.method == 'GET':
            zhibo_id = request.GET.get('id','')                         # 获取直播素材的id
            edite_zhibo = CreativeZhibo.objects.get(pk=zhibo_id)        # 根据id，把这个直播素材对应的数据取出来，展示给前端
            return render(request,'creative/materialCenterBroadcastsEdit.html',{'edite_zhibo':edite_zhibo})

        else :
            id = request.POST.get("id")                                 # 如果编辑素材的话，就得到编辑素材的id
            name = request.POST.get('name')                             # 得到编辑素材的名称
            content = request.POST.get('content')                       # 得到编辑素材的内容
            goods_name = request.POST.get('goods_name')                 # 得到植入商品名称
            memo = request.POST.get('memo')                             # 得到备注内容
            # 得到植入商品的url
            if request.FILES.get('goods_url')=='' or request.FILES.get('goods_url')==None:
                goods_url = request.POST.get('goods_url_name')
            else:
                goods_url = request.FILES.get('goods_url', '')
            # 根据直播素材的id，把编辑好的素材保存到数据库里面
            material = CreativeZhibo.objects.get(pk=id)
            material.name = name
            material.content = content
            material.goods_name = goods_name
            material.goods_url = goods_url
            material.memo = memo
            material.save()
            path = material.archive_url
            save_id = material.pk
            # if path != None:
            '''无论路径是否为空，只要编辑的话，都会重新再打一个新的tar包 '''
            add_edit(request,material,save_id)
            """
                # dir = path.split('.tar')[0]
                # print(dir)
                # file_name = dir.split('/')[-2]
                # print(file_name)
                # txt_name = dir+'.txt'
                # if os.path.exists(path):
                #     os.remove(path)## 删除文件text and tar
                #     os.remove(txt_name)
                #
                #     materialZhibo_dict = CreativeZhibo.objects.values('name','content','goods_name','memo',).filter(pk=id)[0]
                #
                #     text_file = open(dir+'.txt', 'w')
                #     for key in materialZhibo_dict.keys():
                #         if key == 'name':
                #             text_file.write('素材名称'+':')
                #         elif key == 'content':
                #             text_file.write('口播内容'+':')
                #         elif key == 'goods_name':
                #             text_file.write('植入商品'+':')
                #         else:
                #             text_file.write('备注'+':')
                #         text_file.write(materialZhibo_dict[key])
                #         text_file.write('\n')
                #     text_file.close()
                #                     ## 执行linux 命令 生成tar包
                #     os.system('tar -czvf  %s -C %s %s ' % (dir+'.tar', 'media/img_goods/', file_name))
                #
                #     new_Zhibo= CreativeZhibo.objects.get(pk=id)
                #     new_Zhibo.archive_url= dir +'.tar'
                #     new_Zhibo.save()  ## 保存archive_url
                """
            #
            # else:
            #
            # add_edit(request,material,save_id)

            '''
                if material.goods_url.name == '' or material.goods_url.name == None:  # 如果图片没有上传
                    target_files = time.strftime('%Y%m%d%H%M%S')  ## 给txt文件的 上层目录命名, 为了打压缩包
                    files_dir = 'media/img_goods/' + target_files  ## 路径
                    os.system('mkdir %s' % files_dir)  ## 生成目录
                    materialZhibo_dict = \
                    CreativeZhibo.objects.values('name', 'content', 'goods_name', 'memo').filter(pk=save_id)[0]
                    text_path = files_dir + '/' + materialZhibo_dict['name']  ## 生成全路径的txt 名
                    text_file = open(text_path + '.txt', 'w')
                    for key in materialZhibo_dict.keys():
                        if key == 'name':
                            text_file.write('素材名称' + ':')
                        elif key == 'content':
                            text_file.write('口播内容' + ':')
                        elif key == 'goods_name':
                            text_file.write('植入商品' + ':')
                        else:
                            text_file.write('备注' + ':')
                        text_file.write(materialZhibo_dict[key])
                        text_file.write('\n')
                    text_file.close()
                    ## 执行linux 命令 生成tar包
                    os.system('tar -czvf  %s -C %s %s ' % (text_path + '.tar', 'media/img_goods/', target_files))

                    Zhibo = CreativeZhibo.objects.get(pk=save_id)
                    Zhibo.archive_url = text_path + '.tar'
                    Zhibo.save()  ## 保存archive_url

                else:
                    source_file = material.goods_url.name  ## 图像文件在项目中的名字
                    file_name = source_file.split('/')[-1]  ## 文件名
                    files_path = source_file.split(file_name)[0]  ## 文件在项目中的路径
                    index = 'media/' + files_path  ## 展示给用户的路径
                    next_files = files_path.split('/')[2:-1][0]  ## 最后一层文件夹
                    ex_files = index.split(next_files)[0]  ## 除最后一层文件夹外的 项目目录

                    materialZhibo_dict = \
                    CreativeZhibo.objects.values('name', 'content', 'goods_name', 'memo').filter(pk=save_id)[0]
                    text_path = index + materialZhibo_dict['name']

                    if os.path.isdir(text_path):
                        pass
                    else:
                        os.makedirs(text_path)
                        text_file = open(text_path + '.txt', 'w')
                        pass
                    for key in materialZhibo_dict.keys():
                        global  text_file
                        if key == 'name':
                            text_file.write('素材名称' + ':')
                        elif key == 'content':
                            text_file.write('口播内容' + ':')
                        elif key == 'goods_name':
                            text_file.write('植入商品' + ':')
                        else:
                            text_file.write('备注' + ':')
                        text_file.write(materialZhibo_dict[key])
                        text_file.write('\n')
                    text_file.close()

                    ## 执行linux 命令 生成tar包
                    os.system('tar -czvf  %s -C %s %s ' % (text_path + '.tar', ex_files, next_files))

                    new_Zhibo = CreativeZhibo.objects.get(pk=save_id)
                    new_Zhibo.archive_url = text_path + '.tar'
                    new_Zhibo.save()  ## 保存archive_url
                '''





            """
            #materialZhibo_dict = CreativeZhibo.objects.values('name','content','goods_name','memo',).filter(pk=id)[0]
            #
            # text_file = open(dir+'.txt', 'w')
            # for key in materialZhibo_dict.keys():
            #     if key == 'name':
            #         text_file.write('素材名称'+':')
            #     elif key == 'content':
            #         text_file.write('口播内容'+':')
            #     elif key == 'goods_name':
            #         text_file.write('植入商品'+':')
            #     else:
            #         text_file.write('备注'+':')
            #     text_file.write(materialZhibo_dict[key])
            #     text_file.write('\n')
            # text_file.close()
            #                 ## 执行linux 命令 生成tar包
            # os.system('tar -czvf  %s -C %s %s ' % (dir+'.tar', 'media/img_goods/', file_name))
            #
            # new_Zhibo= CreativeZhibo.objects.get(pk=id)
            # new_Zhibo.archive_url= dir +'.tar'
            # new_Zhibo.save()  ## 保存archive_url
            """

            return HttpResponseRedirect('/creative')

    #添加素材
    def add_view(request):
        state =None
        if request.method == 'POST':
            if request.FILES.get('goods_url') == '' or request.FILES.get('goods_url') == None:
                is_uploads = 'B'
            else:
                is_uploads = 'A'
            new_materialZhibo = CreativeZhibo(
                is_upload=is_uploads,  ##A:已上传;B未上传
                name = request.POST.get('name',''),
                content = request.POST.get('content', ''),
                goods_name=request.POST.get('goods_name', ''),
                goods_url=request.FILES.get('goods_url', ''),##图片
                memo=request.POST.get('memo', ''),
            )
            new_materialZhibo.save()
            save_id =new_materialZhibo.pk
            add_edit(request,new_materialZhibo,save_id)

            """
            # print(new_materialZhibo)
            # new_materialZhibo.save()
            # save_id =new_materialZhibo.pk
            # print(save_id)
            #
            # if new_materialZhibo.goods_url.name == '':  # 如果图片没有上传
            #
            #     target_files = time.strftime('%Y%m%d%H%M%S')  ## 给txt文件的 上层目录命名, 为了打压缩包
            #     files_dir = 'media/img_goods/'+target_files   ## 路径
            #     os.system('mkdir %s' % files_dir)             ## 生成目录
            #     new_materialZhibo_dict = CreativeZhibo.objects.values('name','content','goods_name','memo').filter(pk=save_id)[0]
            #     text_path = files_dir +'/'+ new_materialZhibo_dict['name']   ## 生成全路径的txt 名
            #     text_file = open(text_path+'.txt', 'w')
            #     for key in new_materialZhibo_dict.keys():
            #         if key == 'name':
            #             text_file.write('素材名称'+':')
            #         elif key == 'content':
            #             text_file.write('口播内容'+':')
            #         elif key == 'goods_name':
            #             text_file.write('植入商品'+':')
            #         else:
            #             text_file.write('备注'+':')
            #         text_file.write(new_materialZhibo_dict[key])
            #         text_file.write('\n')
            #     text_file.close()
            #                 ## 执行linux 命令 生成tar包
            #     os.system('tar -czvf  %s -C %s %s ' % (text_path+'.tar', 'media/img_goods/', target_files))
            #
            #     new_Zhibo= CreativeZhibo.objects.get(pk=save_id)
            #     new_Zhibo.archive_url= text_path +'.tar'
            #     new_Zhibo.save()  ## 保存archive_url
            #
            # else:
            #
            #     source_file = new_materialZhibo.goods_url.name       ## 图像文件在项目中的名字
            #     print(source_file)
            #     file_name = source_file.split('/')[-1]               ## 文件名
            #     print(file_name)
            #     files_path = source_file.split(file_name)[0]         ## 文件在项目中的路径
            #     print(files_path)
            #     index = 'media/'+files_path                          ## 展示给用户的路径
            #     print(index)
            #
            #     next_files = files_path.split('/')[2:-1][0]          ## 最后一层文件夹
            #     print(next_files)
            #     ex_files = index.split(next_files)[0]                ## 除最后一层文件夹外的 项目目录
            #     print(ex_files)
            #     new_materialZhibo_dict = CreativeZhibo.objects.values('name','content','goods_name','memo').filter(pk=save_id)[0]
            #     print(new_materialZhibo_dict)
            #     text_path = index + new_materialZhibo_dict['name']
            #     print(text_path)
            #     text_file = open(text_path+'.txt', 'w')
            #     print(text_file)
            #     for key in new_materialZhibo_dict.keys():
            #         if key == 'name':
            #             text_file.write('素材名称'+':')
            #         elif key == 'content':
            #             text_file.write('口播内容'+':')
            #         elif key == 'goods_name':
            #             text_file.write('植入商品'+':')
            #         else:
            #             text_file.write('备注'+':')
            #         text_file.write(new_materialZhibo_dict[key])
            #         text_file.write('\n')
            #     text_file.close()
            #
            #     ## 执行linux 命令 生成tar包
            #     os.system('tar -czvf  %s -C %s %s ' % (text_path+'.tar', ex_files, next_files))
            #
            #     new_Zhibo= CreativeZhibo.objects.get(pk=save_id)
            #     new_Zhibo.archive_url= text_path+'.tar'
            #     print(new_Zhibo.archive_url)
            #     new_Zhibo.save()  ## 保存archive_url
            #
            """

            state = 'success'
        content = {
            'active_menu': 'add_creative',
            'state': state,
        }
        return render(request,'creative/materialCenterBroadcasts.html', content)

    #单条 删除 直播素材  (假删除)
    def delete_view(request):
        material_id = request.GET.get('id')
        creativezhibo = CreativeZhibo.objects.get(id=material_id)
        creativezhibo.is_delete=1 #改变直播素材删除状态,id_delete(default=0)
        creativezhibo.save()
        return HttpResponseRedirect('/creative')

    # 批量 删除 直播素材 (假删除)
    def delete_many_view(request):
        if request.method == 'POST' and request.POST.get('materialid')!='':
            material_list_id = request.POST.get('materialid').split(',')
            for material_id in material_list_id:
                creativezhibo = CreativeZhibo.objects.get(pk=int(material_id))
                creativezhibo.is_delete = 1 #改变直播素材删除状态,id_delete(default=0)
                creativezhibo.save()
        return HttpResponseRedirect('/creative')

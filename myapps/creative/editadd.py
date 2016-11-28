from myapps.creative.models import CreativeZhibo
import time
import os

def add_edit(request,new_materialZhibo,save_id):

        if new_materialZhibo.goods_url.name == '' or new_materialZhibo.goods_url.name == None or new_materialZhibo.goods_url.name[28:40] == 'None-img.jpg':  # 如果图片没有上传
            target_files = time.strftime('%Y%m%d%H%M%S')  ## 给txt文件的 上层目录命名, 为了打压缩包
            files_dir = 'media/img_goods/' + target_files  ## 路径
            os.system('mkdir %s' % files_dir)  ## 生成目录
            new_materialZhibo_dict = \
            CreativeZhibo.objects.values('name', 'content', 'goods_name', 'memo').filter(pk=save_id)[0]
            text_path = files_dir + '/' + new_materialZhibo_dict['name']  ## 生成全路径的txt 名
            text_file = open(text_path + '.txt', 'w')
            for key in new_materialZhibo_dict.keys():
                if key == 'name':
                    text_file.write('素材名称' + ':')
                elif key == 'content':
                    text_file.write('口播内容' + ':')
                elif key == 'goods_name':
                    text_file.write('植入商品' + ':')
                else:
                    text_file.write('备注' + ':')
                text_file.write(new_materialZhibo_dict[key])
                text_file.write('\n')
            text_file.close()
            ## 执行linux 命令 生成tar包
            os.system('tar -czvf  %s -C %s %s ' % (text_path + '.tar', 'media/img_goods/', target_files))

            new_Zhibo = CreativeZhibo.objects.get(pk=save_id)
            new_Zhibo.archive_url = text_path + '.tar'
            new_Zhibo.save()  ## 保存archive_url

        else:

            source_file = new_materialZhibo.goods_url.name  ## 图像文件在项目中的名字

            file_name = source_file.split('/')[-1]  ## 文件名

            files_path = source_file.split(file_name)[0]  ## 文件在项目中的路径

            index = 'media/' + files_path  ## 展示给用户的路径


            next_files = files_path.split('/')[2:-1][0]  ## 最后一层文件夹

            ex_files = index.split(next_files)[0]  ## 除最后一层文件夹外的 项目目录

            new_materialZhibo_dict = \
            CreativeZhibo.objects.values('name', 'content', 'goods_name', 'memo').filter(pk=save_id)[0]

            text_path = index + new_materialZhibo_dict['name']

            text_file = open(text_path + '.txt', 'w')

            for key in new_materialZhibo_dict.keys():
                if key == 'name':
                    text_file.write('素材名称' + ':')
                elif key == 'content':
                    text_file.write('口播内容' + ':')
                elif key == 'goods_name':
                    text_file.write('植入商品' + ':')
                else:
                    text_file.write('备注' + ':')
                text_file.write(new_materialZhibo_dict[key])
                text_file.write('\n')
            text_file.close()

            ## 执行linux 命令 生成tar包
            os.system('tar -czvf  %s -C %s %s ' % (text_path + '.tar', ex_files, next_files))

            new_Zhibo = CreativeZhibo.objects.get(pk=save_id)
            new_Zhibo.archive_url = text_path + '.tar'
            new_Zhibo.save()  ## 保存archive_url


copy (select id, name, description
        from project)
  to '/tmp/projects.tsv';

copy (select pdl.parent as project_id, d.id as dataset_id, name, description
        from dataset d, projectdatasetlink pdl
       where d.id = pdl.child and pdl.parent = 501)
  to '/tmp/datasets.tsv';

copy (select d.id as dataset_id, i.id as image_id, i.name, i.description
        from pixels p, image i, datasetimagelink dil, dataset d, projectdatasetlink pdl
       where p.image = i.id and i.id = dil.child and dil.parent = d.id and d.id = pdl.child and pdl.parent = 501)
  to '/tmp/images.tsv';

-- Note: kv also has an "index" since the values are ordered
copy (select i.id as image_id, a.id as annotation_id, a.ns, kv.name, kv.value
        from annotation_mapvalue kv, annotation a, imageannotationlink ial, image i, datasetimagelink dil, dataset d, projectdatasetlink pdl
       where kv.annotation_id = a.id and a.id = ial.child and ial.parent = i.id and i.id = dil.child and dil.parent = d.id and d.id = pdl.child and pdl.parent = 501
       limit 1000
     )
  to '/tmp/image_annotations.tsv';

copy (select d.id as dataset_id, a.id as annotation_id, a.ns, kv.name, kv.value
        from annotation_mapvalue kv, annotation a, datasetannotationlink dal, datasetimagelink dil, dataset d, projectdatasetlink pdl
       where kv.annotation_id = a.id and a.id = dal.child and dal.parent = d.id and d.id = pdl.child and pdl.parent = 501
       limit 1000
     )
  to '/tmp/dataset_annotations.tsv';

copy (select 501 as project_id, a.id as annotation_id, a.ns, kv.name, kv.value
        from annotation_mapvalue kv, annotation a, projectannotationlink pal
       where kv.annotation_id = a.id and a.id = pal.child and pal.parent = 501
       limit 1000
     )
  to '/tmp/project_annotations.tsv';

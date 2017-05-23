/**
 * Created by shendaming on 2017/5/22.
 */

KindEditor.ready(function(K) {
                K.create('textarea[name=content]',{
                    width:'800px',
                    height:'200px',
                    uploadJson: '/admin/upload/kindeditor',
                });
        });
1.�u���O���@�o�^�A�C���A�폜�����ʂ�ǉ�����
2.����̋@�\�����O�C���҂݂̂Ɍ��肵��
�@�������Ȃ�URL����͂��Ă����O�C����ʂɂ����悤�ɂ����B
3.�ŏ��̕\����ʁibase.html)�ɕ\������Ă���J�e�S�����X�g��
�o�^���Ȃ̂ŃJ�e�S���̖��O���ɕ\���������B
 views.py�̒���CategoryViews�́@get_queryset(self):
 ��queryset = Post.objects.order_by('created_at').filter(category=category)
��Category.objects.order_by('name').filter(category=category)
�ƕύX�������A�ς�炸�i�O�̂܂܁ACategory�̓o�^���j
���@Post���f���ƃJ�e�S���̊֌W���ǂ��A�����炢���̂��킩�炸
 ����

�S�D�u���O���폜�����Ƃ��ɁA�߂��ʂ��ŏ��̑S���ꗗ
�ł͂Ȃ��āA�J�e�S���ꗗ���ڍ׉�ʁ��폜�����̃J�e�S���ꗗ
�Ƃ��������A������ǂ������炢�����킩�炸�B
���R�̂��ƂȂ���
DeleteView�� success_url = reverse_lazy('category:index')
�Ƃ�����error�ɂȂ����B�����ł����Ă���index��categor��ID����Ȃ���
POST��ID�����炾�Ǝv�����A�J�e�S���ꗗ����ڍ׉�ʂɈڂ�Ƃ�
����Ȃ��B�����\���̑S���ꗗ����ڍׂɂ����č폜�����Ƃ��ɂ�
�S���ꗗ�ɖ߂�ׂ��E�E�E����͓���B���܁B
5.�ʐ^���A�b�v���[�h�������B�iviews.py�ɏ����̂�CLASS����Ȃ��Ċ֐��ɂ����ق��������̂����H�Y�ށj
�Ƃ������ƂŁA
�܂��܂����������Ƃ���͂��낢�날�邯��ǁA��͂�A�P�P��
�Ӗ���������Ɨ����ł��Ă��Ȃ��̂ł��B







IMAGE_ROOT = OS.path.join(BASE_DIR,'images')
IMAGE_URL = '/images/'
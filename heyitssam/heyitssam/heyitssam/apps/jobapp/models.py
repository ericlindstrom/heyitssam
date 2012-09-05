from django.db import models

class JobAppManager(models.Manager):
    def is_live():
	return super(JobAppManager, self).get_query_set().filter(visible=True)

class JobApp(models.Model):
    company_name = models.CharField(max_length=255)
    slug = models.SlugField()
    position = models.CharField(max_length=255)
    intro = models.TextField()
    objective = models.TextField()
    visible = models.BooleanField(default=True)
    show_cv = models.BooleanField(default=True)
    show_resume = models.BooleanField(default=True)

    objects = JobAppManager()

    def __unicode__(self):
	return self.position

    @models.permalink
    def get_absolute_url(self):
	return ('jobapp:overview', (), { 'slug': self.slug })

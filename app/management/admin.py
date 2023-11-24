from django.contrib import admin
from management import models
from django_admin_relation_links import AdminChangeLinksMixin


@admin.register(models.HeuristicMatching)
class HeuristicMatchingAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user']

    list_display = [
        'heuristic_matching',
        'user_link',
        'execution_time',
        'created_on_datetime',
        'updated_on_datetime'
    ]


@admin.register(models.MaxMatching)
class MaxMatchingAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user']

    list_display = [
        'max_matching',
        'user_link',
        'execution_time',
        'created_on_datetime',
        'updated_on_datetime'
    ]


@admin.register(models.ExecutionHistory)
class ExecutionHistoryAdmin(AdminChangeLinksMixin, admin.ModelAdmin):
    change_links = ['user', 'max_matching', 'heuristic_matching']

    list_display = [
        'max_matching_link',
        'heuristic_matching_link',
        'graph_density',
        'user_link',
        'created_on_datetime',
        'updated_on_datetime'
    ]


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'subject',
    ]
    readonly_fields = [
        'name',
        'email',
        'subject',
        'message'
    ]


admin.site.site_header = 'MAX MATCHING ADMIN'
admin.site.site_title = 'MAX MATCHING'
admin.site.index_title = 'mws - thesis: ali_133380@svuonline.org'

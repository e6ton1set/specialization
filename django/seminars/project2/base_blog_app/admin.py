from django.contrib import admin
from base_blog_app.models import Article, Author, Comment


@admin.action(description="Обнулить счётчик просмотров")
def reset_views(modeladmin, request, queryset):
    queryset.update(show_count=0)


class ArticleAdmin(admin.ModelAdmin):
    # отображение столбцов в таблице
    list_display = ['author', 'title', 'content', 'published', 'category', 'is_published', 'show_count']
    # сортировка столбцов по дате публикации (по убыванию)
    ordering = ('-published',)
    # отображение полей при просмотре страницы, редактировании и созранении
    readonly_fields = ('author', 'published', 'show_count')
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['author', 'title'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Содержание статьи',
                'fields': ['content', 'category'],
            },
        ),
        (
            'Дата создания и настройки публикации',
            {
                'fields': ['published', 'is_published'],
            },
        ),
    ]
    search_fields = ['title', 'content']
    list_filter = ['show_count']
    list_per_page = 15
    actions = [reset_views]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Comment)

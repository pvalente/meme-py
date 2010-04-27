from meme import MemeRepository, PostRepository

class Meme(object):
    meme_repository = MemeRepository()
    
    @staticmethod
    def get(name=None):
        '''Gets a Meme by it's name/user, e.g.: "gchapiewski".'''
        return Meme.meme_repository.get(name)
    
    @staticmethod
    def get_by_guid(guid=None):
        '''Gets a Meme by it's guid, e.g.: "ZZR4B57H4FTGKOC4AUWPOY4FWM".'''
        return Meme.meme_repository.get_by_guid(guid)

    @staticmethod
    def search(query, count=10):
        '''Searches for Memes that have the title similar to the search string.'''
        return Meme.meme_repository.search(query, count)
    
    class Posts(object):
        post_repository = PostRepository()
        
        @staticmethod
        def get(owner_guid, pubid):
            '''Gets one post.'''
            return Meme.Posts.post_repository.get(owner_guid, pubid)

        @staticmethod
        def popular(locale='en', count=10):
            '''Gets the popular posts.'''
            return Meme.Posts.post_repository.popular(locale, count)
        
        @staticmethod
        def search(query, count=10):
            '''Searches for Posts that contains the specified word(s).'''
            return Meme.Posts.post_repository.search(query, count)
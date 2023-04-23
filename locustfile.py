import random
from locust import HttpUser, task, constant, between

class FringeUser(HttpUser):

    wait_time = between(10, 30)
    festival_year = '2022'
    day_num_min = 19978
    day_num_max = 19988

    def on_start(self):
        self.day = random.randrange(self.day_num_min, self.day_num_max)

    @task
    def load_shows_list(self):
        self.client.get(f'/{self.festival_year}/shows')

    @task
    def load_schedule(self):
        self.client.get(f"/{self.festival_year}/schedule?d={self.day}")

    @task
    def load_schedule_grid(self):
        self.client.get(f"/{self.festival_year}/schedule-grid?d={self.day}")

    @task
    def load_random_show_page(self):
        # self.client.get("/2022-show-information/who-s-afraid-of-winnie-the-pooh-")
        self.client.get(random.choice(self.show_urls_list))

    show_urls_list = [
        '/2022-show-information/desi-heart-crust',
        '/2022-show-information/endometriosis-the-musical',
        '/2022-show-information/she-s-already-gone',
        '/2022-show-information/finger-lickin-good',
        '/2022-show-information/a-drug-play',
        '/2022-show-information/_rsg-ng-what-you-follow-follows-you',
        '/2022-show-information/bob-and-reggie-go-to-bed',
        '/2022-show-information/swords-sorcery-the-improvised-fantasy-campaign',
        '/2022-show-information/who-s-afraid-of-winnie-the-pooh-',
        '/2022-show-information/orzel-rising',
        '/2022-show-information/swim-team',
        '/2022-show-information/a-day-with-the-newhearts',
        '/2022-show-information/moonwatchers',
        '/2022-show-information/3-guys-on-stage-who-get-hit-with-hot-dogs-snow-cones-etc-',
        '/2022-show-information/erotica-for-houseplants',
        '/2022-show-information/pop-sensationz-',
        '/2022-show-information/developers-',
        '/2022-show-information/silver-hammer',
        '/2022-show-information/_whoosh-the-civil-war-mythology-of-michael-hickey-and-his-perilous-precipitation-over-st-anthony-falls-',
        '/2022-show-information/shoe-night',
        '/2022-show-information/the-hysterical-woman',
        '/2022-show-information/turnabout-samurai',
        '/2022-show-information/connor-s-gonna-tell-the-t-in-b-c-ailnge',
        '/2022-show-information/slender-vale',
        '/2022-show-information/becoming-baba-yaga',
        '/2022-show-information/jesus-qhrist',
        '/2022-show-information/jon-bennett-fire-in-the-meth-lab',
        '/2022-show-information/rewrites',
        '/2022-show-information/the-witchy-world-of-luna-muse',
        '/2022-show-information/help-me-help-you-help-yourself',
        '/2022-show-information/neil-gaiman-s-the-wedding-present-',
        '/2022-show-information/action-will-be-taken-an-action-packed-play-',
        '/2022-show-information/on-a-stick-a-minnesota-state-fair-musical',
        '/2022-show-information/cowboy-widow-a-honkytonk-musical',
        '/2022-show-information/pi-ata',
        '/2022-show-information/5-first-dates',
        '/2022-show-information/black-wall-street-dreamland-theatre',
        '/2022-show-information/the-real-black-swann-confessions-of-america-s-first-black-drag-queen-',
        '/2022-show-information/unbelievable-',
        '/2022-show-information/cowboy-cat-the-musical-',
        '/2022-show-information/karaoke-after-dark',
        '/2022-show-information/paper-soul',
        '/2022-show-information/peace-retreat',
        '/2022-show-information/bellerophon-s-shadow-voyage-of-the-pegasus-',
        '/2022-show-information/fleeting-an-eco-comedy-absurdist-rant',
        '/2022-show-information/i-love-my-body-and-it-s-trying-to-kill-me',
        '/2022-show-information/my-empty-arms',
        '/2022-show-information/one-woman-beaches-',
        '/2022-show-information/the-shrieking-harpies',
        '/2022-show-information/penelope',
        '/2022-show-information/can-i-interest-you-in-me-',
        '/2022-show-information/curtain-call-letters-to-my-friend-louie-anderson-',
        '/2022-show-information/joter-a-our-untold-stories-',
        '/2022-show-information/michael-bay-s-bridgerton-vii-revenge-of-the-forlorn',
        '/2022-show-information/sunshine-by-adam-szudrich',
        '/2022-show-information/bonny-read',
        '/2022-show-information/he-man-is-the-devil-other-satanic-panic-tales',
        '/2022-show-information/people-r-ready-the-musical',
        '/2022-show-information/traitor',
        '/2022-show-information/what-takes-who',
        '/2022-show-information/burr-a-new-musical',
        '/2022-show-information/icterine',
        '/2022-show-information/my-lovely-lovely-lovely-lovely-lovely-family',
        '/2022-show-information/newton-jr-',
        '/2022-show-information/shmilf-life',
        '/2022-show-information/all-we-ever-wanted-was-everything',
        '/2022-show-information/ancestors-rising',
        '/2022-show-information/beach-play',
        '/2022-show-information/i-think-we-are-supposed-to-be-coming-of-age-by-now-',
        '/2022-show-information/life-underground',
        '/2022-show-information/my-dance-with-lisa-',
        '/2022-show-information/virality',
        '/2022-show-information/we-are-the-sea',
        '/2022-show-information/what-s-your-day-job-or-how-capitalism-destroys-us-all-',
        '/2022-show-information/aureate',
        '/2022-show-information/dead-mother-s-underwear',
        '/2022-show-information/francis-e-fingerbowl-has-gone-missing-',
        '/2022-show-information/happy-endings-church-a-haggardly-tale-of-woe-redemption',
        '/2022-show-information/the-biggest-wail-from-the-bottom-of-my-heart',
        '/2022-show-information/a-little-water',
        '/2022-show-information/dark-pony-radio-an-evening-with-the-oupire-',
        '/2022-show-information/hope',
        '/2022-show-information/stages-a-horror-play',
        '/2022-show-information/the-man-from-earth',
        '/2022-show-information/the-unboxing',
        '/2022-show-information/babel-s-banging-binders',
        '/2022-show-information/daybreak-diner',
        '/2022-show-information/the-3-way-',
        '/2022-show-information/changing-the-narrative-climate-stories-for-justice',
        '/2022-show-information/cupcake-murders-a-ballet',
        '/2022-show-information/foreigner-frenzy-the-mast-diaries-of-1978-',
        '/2022-show-information/lot-o-shakespeare',
        '/2022-show-information/the-brothers-dangus-vol-1-the-liturgy-of-the-big-yellow-ghost',
        '/2022-show-information/wounded-healers',
        '/2022-show-information/expiration-date',
        '/2022-show-information/gemini-a-magic-show-',
        '/2022-show-information/hi-my-name-is-',
        '/2022-show-information/pajama-stories-for-children-all-adults-only-',
        '/2022-show-information/the-conversation',
        '/2022-show-information/able-to-',
        '/2022-show-information/in-this-house',
        '/2022-show-information/stranger-vs-the-malevolent-malignancy',
        '/2022-show-information/the-killing-of-eve',
        '/2022-show-information/the-local-music-scene',
        '/2022-show-information/the-marvelous-magpie-moon',
        '/2022-show-information/it-s-going-down-in-uptown',
        '/2022-show-information/the-best-jester',
        '/2022-show-information/dancing-through-egypt',
        '/2022-show-information/infinity-hour',
        '/2022-show-information/prosperity-gospel-',
        '/2022-show-information/stars-of-the-twin-cities-',
        '/2022-show-information/the-dog-show',
        '/2022-show-information/the-humor-of-pat-ryan-and-parkinson-s-part-2-the-miracle',
    ]

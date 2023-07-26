import random
from locust import HttpUser, task, constant, between

class FringeUser(HttpUser):

    wait_time = between(3, 15)
    festival_year = '2023'
    day_num_min = 3
    day_num_max = 13

    def on_start(self):
        self.date = '2023-08-%(day)02d' % {"day": random.randint(self.day_num_min, self.day_num_max)}

    @task
    def load_shows_list(self):
        # self.client.get(f'/shows/{self.festival_year}')
        # page actually has "Load More" appending paging, only loads 1 batch
        # /shows/2023?&prop_ModuleId=39277&page=2
        page = random.randint(1,6)
        self.client.get(f'/shows/{self.festival_year}?&prop_ModuleId=39277&page={page}')

    @task
    def load_schedule(self):
        # https://minnesotafringe.org/schedule/2023?d=2023-08-03#schedule
        self.client.get(f"/schedule/{self.festival_year}?d={self.date}")

    @task
    def load_schedule_grid(self):
        self.client.get(f"/schedule-grid/{self.festival_year}?d={self.date}")

    @task
    def load_random_show_page(self):
        # self.client.get("/2022-show-information/who-s-afraid-of-winnie-the-pooh-")
        self.client.get(random.choice(self.show_urls_list[2023]))

    show_urls_list = {
        2023: [
            '/shows/2023/101-goofin-things',
            '/shows/2023/1992-mistakes-were-made-',
            '/shows/2023/20-000-leagues-under-the-telltale-heart',
            '/shows/2023/4-bisexuals-and-2-guys-named-john-kill-dracula',
            '/shows/2023/5-prisoners',
            '/shows/2023/5-step-guide-to-being-german',
            '/shows/2023/absurdity-a-burlesque-experience',
            '/shows/2023/adaptopus',
            '/shows/2023/a-girl-scout-s-guide-to-exorcism-',
            '/shows/2023/a-jingle-jangle-morning',
            '/shows/2023/allegro',
            '/shows/2023/apocalypse-later-i-love-the-smell-of-procrastination-in-the-morning',
            '/shows/2023/a-swimming-lesson-in-a-theatre-without-a-lifeguard',
            '/shows/2023/audacious-ignatius-lost-in-atlantis',
            '/shows/2023/baldwin-s-last-fire',
            '/shows/2023/behemoth',
            '/shows/2023/betsy-show',
            '/shows/2023/big-dad-energy',
            '/shows/2023/born-of-a-fairy-tale',
            '/shows/2023/boy-crazy',
            '/shows/2023/breakneck-midsummer-night-s-dream',
            '/shows/2023/brutus',
            '/shows/2023/butts-in-seats-how-to-get-people-to-attend-your-shakespeare-production-by-having-musical-settings-for-the-lyrics-in-his-plays-numerous-examples-included-',
            '/shows/2023/choose-your-own-fringe-adventure',
            '/shows/2023/chris-davis-does-stuff',
            '/shows/2023/climbing-my-family-tree-',
            '/shows/2023/comedy-vs-calories-chaos-',
            '/shows/2023/coyfish',
            '/shows/2023/dearest-mother',
            '/shows/2023/dock-work',
            '/shows/2023/doline-emerging-into-the-light',
            '/shows/2023/dolly-who-',
            '/shows/2023/epimetheus',
            '/shows/2023/everything-bagel',
            '/shows/2023/extreme-roadshow',
            '/shows/2023/fargo-allegro',
            '/shows/2023/fire-in-my-veins-blazing-through-life-with-invisible-illness',
            '/shows/2023/float',
            '/shows/2023/funny-like-an-abortion',
            '/shows/2023/gilda-a-tribute-to-the-beloved-comedienne-gilda-radner',
            '/shows/2023/grindr-help-desk-the-musical',
            '/shows/2023/ha-ha-da-vinci',
            '/shows/2023/in-celebration-of-the-mysterious-',
            '/shows/2023/john-wick-by-tim-wick-no-relation-',
            '/shows/2023/jonah-joanna-and-the-great-big-fish',
            '/shows/2023/joy-a-sketch-show',
            '/shows/2023/kill-b-the-epilogue',
            '/shows/2023/kill-me-too',
            '/shows/2023/let-me-say-this-about-that',
            '/shows/2023/little-pieces',
            '/shows/2023/lost-in-bear-country-birth-god-death-and-the-berenstain-bears',
            '/shows/2023/mischief-in-ink-the-school-prank-of-03',
            '/shows/2023/mother-courage-bear-and-her-children',
            '/shows/2023/my-only-hope-for-a-hero',
            '/shows/2023/new-origins-beauty-and-the-beast',
            '/shows/2023/npc-non-player-character-',
            '/shows/2023/old-habits-a-dragtastrophe',
            '/shows/2023/omar-khayyam-club',
            '/shows/2023/open-mic-at-the-dream-shop-',
            '/shows/2023/opera-punks',
            '/shows/2023/patolog-a-or-fagology-',
            '/shows/2023/pearl-and-eugene-one-last-shtick',
            '/shows/2023/phoenix-presents',
            '/shows/2023/pillow-talk',
            '/shows/2023/playback-time',
            '/shows/2023/primary',
            '/shows/2023/rails-',
            '/shows/2023/reception',
            '/shows/2023/reincarnation-soup',
            '/shows/2023/rope-dances',
            '/shows/2023/shark-grant',
            '/shows/2023/stabby-stab-stab',
            '/shows/2023/star-trek-the-next-improvisation-presented-by-huge-theater',
            '/shows/2023/_starved-the-astonishing-true-story-of-the-university-of-minnesota-starvation-experiment',
            '/shows/2023/tales-from-the-fiefdom',
            '/shows/2023/the-brothers-dangus-vol-2-the-people-v-dango-a-court-mandated-parable-',
            '/shows/2023/the-definition-of-loss',
            '/shows/2023/the-duet',
            '/shows/2023/the-falsehood',
            '/shows/2023/the-place-i-return-to',
            '/shows/2023/the-resilient-child',
            '/shows/2023/the-shrieking-harpies',
            '/shows/2023/the-spell-of-the-yukon',
            '/shows/2023/the-very-model-of-a-modern-monster-scientist',
            '/shows/2023/the-windblown-cheeks-of-lovers',
            '/shows/2023/thousand-pears',
            '/shows/2023/too-many-notes',
            '/shows/2023/truth-or-truth',
            '/shows/2023/two-stars-in-the-vast-dark',
            '/shows/2023/uncle-walt',
            '/shows/2023/veriites',
            '/shows/2023/we-can-wish-a-beatboxing-and-music-variety-show',
            '/shows/2023/_well-made-bread',
            '/shows/2023/wells-is-third-on-the-waitlist',
            '/shows/2023/west-bank-neighborhood-history-walking-tour',
            '/shows/2023/when-you-hear-the-chime-',
            '/shows/2023/works-in-progress',
            '/shows/2023/write-me-letters',
            '/shows/2023/yes-no-maybe-please-explain-',
        ],
        2022: [
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
    }

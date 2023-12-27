# This configuration prepares AIHUB 한국어글자체이미지 dataset
# Read https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=81 for more info.
data_root = 'data/text_in_the_wild'
cache_path = 'data/cache'

train_preparer = dict(
    obtainer=dict(
        type='NaiveObtainer',
        cache_path=cache_path,
        files=[
            dict(

            )
        ]

    )
)

# Not Complete Code 
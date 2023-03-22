from argparse import ArgumentParser

from aiohttp.web import Application
from aiohttp_jinja2 import setup as setup_jinja
from jinja2.loaders import PackageLoader
from trafaret_config import commandline

from sqli.middlewares import session_middleware, error_middleware
from sqli.schema.config import CONFIG_SCHEMA
from sqli.services.db import setup_database
from sqli.services.redis import setup_redis
from sqli.utils.jinja2 import csrf_processor, auth_user_processor
from .routes import setup_routes


def init(argv):
    ap = ArgumentParser()
    commandline.standard_argparse_options(ap, default_config='./config/dev.yaml')
    options = ap.parse_args(argv)

    config = commandline.config_from_options(options, CONFIG_SCHEMA)

    app = Application(
        debug=True,
        middlewares=[
            session_middleware,
            # csrf_middleware,
            error_middleware,
        ]
    )
    app['config'] = config

    setup_jinja(app, loader=PackageLoader('sqli', 'templates'),
                context_processors=[csrf_processor, auth_user_processor],
                autoescape=False)
    setup_database(app)
    setup_redis(app)
    setup_routes(app)

    return app


def gets3():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE30110/2DWbl'

def gets4():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE30210/2DWbl'

def gets50008():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50008/2DWbl'
def gets50009():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50009/2DWbl'
def gets50010():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50010/2DWbl'
def gets50011():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50011/2DWbl'
def gets50012():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50012/2DWbl'
def gets50013():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50013/2DWbl'
def gets50014():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50014/2DWbl'
def gets50015():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50015/2DWbl'
def gets50016():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50016/2DWbl'
def gets50017():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50017/2DWbl'
def gets50018():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50018/2DWbl'
def gets50019():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50019/2DWbl'
def gets50020():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50020/2DWbl'
def gets50021():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50021/2DWbl'
def gets50022():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50022/2DWbl'
def gets50023():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50023/2DWbl'
def gets50024():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50024/2DWbl'
def gets50025():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50025/2DWbl'
def gets50026():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50026/2DWbl'
def gets50027():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50027/2DWbl'
def gets50028():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50028/2DWbl'
def gets50029():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50029/2DWbl'
def gets50030():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50030/2DWbl'
def gets50031():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50031/2DWbl'
def gets50032():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50032/2DWbl'
def gets50033():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50033/2DWbl'
def gets50034():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50034/2DWbl'
def gets50035():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50035/2DWbl'
def gets50036():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50036/2DWbl'
def gets50037():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50037/2DWbl'
def gets50038():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50038/2DWbl'
def gets50039():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50039/2DWbl'
def gets50040():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50040/2DWbl'
def gets50041():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50041/2DWbl'
def gets50042():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50042/2DWbl'
def gets50043():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50043/2DWbl'
def gets50044():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50044/2DWbl'
def gets50045():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50045/2DWbl'
def gets50046():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50046/2DWbl'
def gets50047():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50047/2DWbl'
def gets50048():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50048/2DWbl'
def gets50049():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50049/2DWbl'
def gets50050():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50050/2DWbl'
def gets50051():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50051/2DWbl'
def gets50052():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50052/2DWbl'
def gets50053():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50053/2DWbl'
def gets50054():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50054/2DWbl'
def gets50055():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50055/2DWbl'
def gets50056():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50056/2DWbl'
def gets50057():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50057/2DWbl'
def gets50058():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50058/2DWbl'
def gets50059():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50059/2DWbl'
def gets50060():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50060/2DWbl'
def gets50061():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50061/2DWbl'
def gets50062():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50062/2DWbl'
def gets50063():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50063/2DWbl'
def gets50064():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50064/2DWbl'
def gets50065():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50065/2DWbl'
def gets50066():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50066/2DWbl'
def gets50067():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50067/2DWbl'
def gets50068():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50068/2DWbl'
def gets50069():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50069/2DWbl'
def gets50070():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50070/2DWbl'
def gets50071():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50071/2DWbl'
def gets50072():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50072/2DWbl'
def gets50073():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50073/2DWbl'
def gets50074():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50074/2DWbl'
def gets50075():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50075/2DWbl'
def gets50076():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50076/2DWbl'
def gets50077():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50077/2DWbl'
def gets50078():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE50078/2DWbl'
def gets59817():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59817/2DWbl'
def gets59818():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59818/2DWbl'
def gets59819():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59819/2DWbl'
def gets59820():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59820/2DWbl'
def gets59821():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59821/2DWbl'
def gets59822():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59822/2DWbl'
def gets59823():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59823/2DWbl'
def gets59824():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59824/2DWbl'
def gets59825():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59825/2DWbl'
def gets59826():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59826/2DWbl'
def gets59827():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59827/2DWbl'
def gets59828():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59828/2DWbl'
def gets59829():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59829/2DWbl'
def gets59830():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59830/2DWbl'
def gets59831():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59831/2DWbl'
def gets59832():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59832/2DWbl'
def gets59833():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59833/2DWbl'
def gets59834():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59834/2DWbl'
def gets59835():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59835/2DWbl'
def gets59836():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59836/2DWbl'
def gets59837():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59837/2DWbl'
def gets59838():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59838/2DWbl'
def gets59839():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59839/2DWbl'
def gets59840():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59840/2DWbl'
def gets59841():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59841/2DWbl'
def gets59842():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59842/2DWbl'
def gets59843():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59843/2DWbl'
def gets59844():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59844/2DWbl'
def gets59845():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59845/2DWbl'
def gets59846():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59846/2DWbl'
def gets59847():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59847/2DWbl'
def gets59848():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59848/2DWbl'
def gets59849():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59849/2DWbl'
def gets59850():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59850/2DWbl'
def gets59851():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59851/2DWbl'
def gets59852():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59852/2DWbl'
def gets59853():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59853/2DWbl'
def gets59854():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59854/2DWbl'
def gets59855():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59855/2DWbl'
def gets59856():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59856/2DWbl'
def gets59857():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59857/2DWbl'
def gets59858():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59858/2DWbl'
def gets59859():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59859/2DWbl'
def gets59860():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59860/2DWbl'
def gets59861():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59861/2DWbl'
def gets59862():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59862/2DWbl'
def gets59863():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59863/2DWbl'
def gets59864():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59864/2DWbl'
def gets59865():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59865/2DWbl'
def gets59866():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59866/2DWbl'
def gets59867():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59867/2DWbl'
def gets59868():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59868/2DWbl'
def gets59869():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59869/2DWbl'
def gets59870():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59870/2DWbl'
def gets59871():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59871/2DWbl'
def gets59872():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59872/2DWbl'
def gets59873():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59873/2DWbl'
def gets59874():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59874/2DWbl'
def gets59875():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59875/2DWbl'
def gets59876():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59876/2DWbl'
def gets59877():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59877/2DWbl'
def gets59878():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59878/2DWbl'
def gets59879():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59879/2DWbl'
def gets59880():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59880/2DWbl'
def gets59881():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59881/2DWbl'
def gets59882():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59882/2DWbl'
def gets59883():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59883/2DWbl'
def gets59884():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59884/2DWbl'
def gets59885():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59885/2DWbl'
def gets59886():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59886/2DWbl'
def gets59887():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59887/2DWbl'
def gets59888():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59888/2DWbl'
def gets59889():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59889/2DWbl'
def gets59890():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59890/2DWbl'
def gets59891():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59891/2DWbl'
def gets59892():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59892/2DWbl'
def gets59893():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59893/2DWbl'
def gets59894():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59894/2DWbl'
def gets59895():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59895/2DWbl'
def gets59896():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59896/2DWbl'
def gets59897():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59897/2DWbl'
def gets59898():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59898/2DWbl'
def gets59899():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59899/2DWbl'
def gets59900():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59900/2DWbl'
def gets59901():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59901/2DWbl'
def gets59902():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59902/2DWbl'
def gets59903():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59903/2DWbl'
def gets59904():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59904/2DWbl'
def gets59905():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59905/2DWbl'
def gets59906():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59906/2DWbl'
def gets59907():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59907/2DWbl'
def gets59908():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59908/2DWbl'
def gets59909():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59909/2DWbl'
def gets59910():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59910/2DWbl'
def gets59911():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59911/2DWbl'
def gets59912():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59912/2DWbl'
def gets59913():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59913/2DWbl'
def gets59914():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59914/2DWbl'
def gets59915():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59915/2DWbl'
def gets59916():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59916/2DWbl'
def gets59917():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59917/2DWbl'
def gets59918():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59918/2DWbl'
def gets59919():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59919/2DWbl'
def gets59920():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59920/2DWbl'
def gets59921():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59921/2DWbl'
def gets59922():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59922/2DWbl'
def gets59923():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59923/2DWbl'
def gets59924():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59924/2DWbl'
def gets59925():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59925/2DWbl'
def gets59926():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59926/2DWbl'
def gets59927():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59927/2DWbl'
def gets59928():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59928/2DWbl'
def gets59929():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59929/2DWbl'
def gets59930():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59930/2DWbl'
def gets59931():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59931/2DWbl'
def gets59932():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59932/2DWbl'
def gets59933():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59933/2DWbl'
def gets59934():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59934/2DWbl'
def gets59935():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59935/2DWbl'
def gets59936():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59936/2DWbl'
def gets59937():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59937/2DWbl'
def gets59938():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59938/2DWbl'
def gets59939():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59939/2DWbl'
def gets59940():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59940/2DWbl'
def gets59941():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59941/2DWbl'
def gets59942():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59942/2DWbl'
def gets59943():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59943/2DWbl'
def gets59944():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59944/2DWbl'
def gets59945():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59945/2DWbl'
def gets59946():
    AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE59946/2DWbl'

AWS_ACCESS_KEY = 'AKIAQWESQRFOQ4KOQAPK'
AWS_SECRET_KEY = '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'
AWS_CONSOLE_PASSWORD = '$ecureAdmin1000'
AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE10000/2DWbl'
AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE20000/2DWbl'
AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE20001/2DWbl'
AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE30000/2DWbl'
AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE30001/2DWbl'
AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE40000/2DWbl'
AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE20011/2DWbl'
AWS_SECRET_KEY = 'SDyoOe0/so/muXBufjrQs9wDcFCsE30010/2DWbl'

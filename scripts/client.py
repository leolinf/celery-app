# coding: utf-8
from bin.tasks import app


def main():
    app.send_task('rd.group.qudao.no_trade_alert.inspect', args=(True, ))


if __name__ == '__main__':
    main()

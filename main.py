from confReader.confReader import read_file
from server.server import Server


if __name__ == '__main__':
    config = read_file('config')
    print(config)
    server = Server(config['host'], config['port'], 'hand')
    server.start(int(config['cpu']), int(config['threads']))
    print('Server started.')
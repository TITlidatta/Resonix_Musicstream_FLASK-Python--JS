from .database import db


class Album(db.Model):
    __tablename__ = "Album"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Artist = db.Column(db.String(100), nullable=False)
    Genre = db.Column(db.String(100))


class Playlist(db.Model):
    __tablename__ = "Playlist"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    creator = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    
class Cluster(db.Model):
    __tablename__ = "Cluster"
    sid = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String(100))
    uid = db.Column(db.Integer)
    count = db.Column(db.Integer)


class PlaylistSongs(db.Model):
    __tablename__ = "PlaylistSongs"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True, nullable=False)
    playlistid = db.Column(db.Integer, nullable=False)
    Songsid = db.Column(db.Integer, nullable=False)


class Users(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True, nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(20))
    name = db.Column(db.String(100))

class songs(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    Name = db.Column(db.String(100), nullable=False)
    Artist = db.Column(db.String(100), nullable=False)
    Albumid= db.Column(db.Integer)
    Genre = db.Column(db.String(50))
    lyrics = db.Column(db.String(4000))
    links=db.Column(db.String(4000),nullable=False)
    pics=db.Column(db.String(4000),nullable=False)

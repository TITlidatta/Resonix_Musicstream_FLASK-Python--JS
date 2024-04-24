from flask import Flask , request,Response
from flask import render_template
from flask import jsonify,url_for,redirect
from flask import current_app as app
from .models import Users, Album , songs , PlaylistSongs , Playlist ,Cluster
from .database import db
from data_scienceML.ml import findL
from sqlalchemy import func
import ast

def setup_routes(app):
    @app.route("/login",methods=["GET","POST"])
    def login():
        if request.method == "GET":
            return render_template("signin.html")
        else:
            showx= request.get_json()
            print(showx)
            if showx['role']=='1':
                x=Users.query.filter(Users.Email==showx['username']).first()
                if(x):
                    return jsonify({'redirect_url': url_for("user",id=x.id)})
                else:
                    newu=Users(Email=showx['username'],type='user')
                    db.session.add(newu)
                    db.session.commit()
                    xn=Users.query.filter(Users.Email==showx['username']).first()
                    return jsonify({'redirect_url': url_for("user",id=xn.id)})
            elif showx['role']=='2':
                x=Users.query.filter(Users.Email==showx['username']).first()
                if(x):
                    return jsonify({'redirect_url': url_for("creator",nm=x.name)})
                else:
                    ncv=Users(Email=showx['username'],type='creator')
                    db.session.add(ncv)
                    db.session.commit()
                    return jsonify({'redirect_url': url_for("creator",nm='None')})
            else:
                return jsonify({'redirect_url': url_for("admin")})
                
      

    @app.route("/check/<int:id>", methods=["GET","POST"])
    def check(id) :
        song = songs.query.filter_by(id=id).first()  # Assuming the song with ID 1
        mp3_data = song.links
        return Response(mp3_data, mimetype="audio/mpeg")
    
    @app.route("/user/<int:id>", methods=["GET","POST"])
    def user(id) :
        song = songs.query.all()
        Plax= Playlist.query.filter(Playlist.creator == id).all()
        C=Cluster.query.filter(Cluster.uid==id).group_by(Cluster.genre).order_by(func.count(Cluster.genre).desc()).limit(2).all()
        D=[]
        if(C):
            for i in C:
                D.append(i.genre)
        
            W=findL(D[0],D[1])
            for jj in W:
                jj=', '.join(map(str,jj))
        else:
            W=[]

        L = [
               {
                'id': ss.id,
                'Name': ss.Name,
                'Artist': ss.Artist,
                'pics': ss.pics,
            }
            for ss in song
            ]
        if(Plax):
            P = [
                {
                    'id': ss.id,
                    'Name': ss.Name,
                }
                for ss in Plax
                ]
        else:
            P=[]

        if (len(Plax)>0):
            print(Plax)
            flag=True
        else:
            flag=False
        print(flag)
        return render_template('userAct.html',flag=flag,L=L,P=P,R=[],idx=id,W=W)
    
    @app.route("/admin",methods=["GET","POST"])
    def admin():
        Cn = Users.query.filter(Users.type=='creator').count()
        Un = Users.query.filter(Users.type=='user').count()
        Tn = db.session.query(songs).count()
        An = db.session.query(Album).count()
        return render_template("adminDash.html",Cn=Cn,Tn=Tn,Un=Un,An=An)
    @app.route("/page/<int:id>",methods=["GET"])
    def page(id):
        song = songs.query.filter_by(id=id).first()
        i = {
                'id': song.id,
                'Name': song.Name,
                'Artist': song.Artist,
                'lyrics': song.lyrics,
                'pics': song.pics,
            }
        return render_template("view.html",i=i)
    
    @app.route("/playp/<int:id>",methods=["GET","POST"])
    def playp(id):
        return jsonify({'redirect_url': url_for("playpnow",id=id)})
        
    @app.route("/playpnow/<int:id>",methods=["GET"])
    def playpnow(id):
        print(id)
        conn = PlaylistSongs.query.filter(PlaylistSongs.playlistid==id).all()
        H=[]
        for i in conn:
            H.append(i.Songsid)
        print(H)
        so = songs.query.filter(songs.id.in_(H)).all()
        L = [
               {
                'id': ss.id,
                'Name': ss.Name,
                'Artist': ss.Artist,
                'pics': ss.pics,
            }
            for ss in so
            ]
        return render_template("play.html",L=L,flag=0,nm="None",id=0)
    
    @app.route("/addpl/<int:id>/<string:nam>",methods=["GET","POST"])
    def addpl(id,nam):
        new_user = Playlist(Name=nam,creator=id)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'statusofit': 'ok'})
    
    @app.route("/addtopl/<string:nam>/<int:idx>",methods=["GET","POST"])
    def addtopl(nam,idx):
        print('here',nam,idx)
        plname=Playlist.query.filter(Playlist.Name==nam).first()
        pid=plname.id
        new_user = PlaylistSongs(playlistid=pid,Songsid=idx)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'statusofit': 'ok'})
    
    @app.route("/about",methods=["GET","POST"])
    def about():
        return render_template("aboutReso.html")
    
    @app.route("/logout/<int:idx>",methods=["GET","POST"])
    def logout(idx):
        userx=Users.query.filter(Users.id==idx).first()
        db.session.delete(userx)
        db.session.commit()
        Playo=Playlist.query.filter(Playlist.creator==idx).all()
        H=[]
        for i in Playo:
            H.append(i.id)
        for playlist in Playo:
            db.session.delete(playlist)
        db.session.commit()
        ppx=PlaylistSongs.query.filter(PlaylistSongs.playlistid.in_(H)).all()
        for playlist in ppx:
            db.session.delete(playlist)
        db.session.commit()
        return render_template("signin.html")
        
    @app.route("/creator/<string:nm>",methods=["GET","POST"])
    def creator(nm):
        Cidc=Users.query.filter(Users.name==nm).first()
        if(Cidc):
            idxc=Cidc.id
            Cson=songs.query.filter(songs.Artist==nm).all()
            L=[]
            print('HEEEEEEERRREEEEE')
            L = [
                    {
                        'id': ss.id,
                        'Name': ss.Name,
                        'pics': ss.pics,
                    }
                    for ss in Cson
                ]
            CAlx=Album.query.filter(Album.Artist==nm).all()
            CAl=[]
            CAl= [
                    {
                    'id': ss.id,
                    'Name': ss.Name,
                }
                for ss in CAlx
                ]
            print(L,nm)
        else:
            L=[]
            A=[]
            idxc=0

        return render_template("Creator.html",L=L,nam=nm,A=CAl,idxc=idxc)
    
    @app.route("/visit/<string:nm>",methods=["GET","POST"])
    def visit(nm):
        Cson=songs.query.filter(songs.Artist==nm).all()
        L=[]
        print('HEEEEEEERRREEEEE')
        L = [
               {
                'id': ss.id,
                'Name': ss.Name,
                'pics': ss.pics,
            }
            for ss in Cson
            ]
        return render_template("Allsong.html",L=L)

    @app.route("/Albuma/<int:idd>",methods=["GET","POST"])
    def Albuma(idd):
        return jsonify({'redirect_url': url_for("Albumax",idd=idd)})
    
    @app.route("/Albumax/<int:idd>",methods=["GET","POST"])
    def Albumax(idd):
        print("hererererererere")
        bv=Album.query.filter(Album.id==idd).first()
        nm=bv.Artist
        Cson=songs.query.filter(songs.Albumid==idd).all()
        L=[]
        print('HEEEEEEERRREEEEE')
        L = [
               {
                'id': ss.id,
                'Name': ss.Name,
                'pics': ss.pics,
            }
            for ss in Cson
            ]
        return render_template("play.html",L=L,flag=1,nm=nm,id=idd)
    
    @app.route("/addsl/<string:nm>",methods=["GET","POST"])
    def addsl(nm):
        if request.method == 'POST':
            print('herererererccxxddegfdgj')
            name = request.form['Name']
            lyrics = request.form['Lyrics']
            genre = request.form['Genre']
            poster = request.form['Poster']
            mp3_file = request.files['song']
            mp3_bytes = mp3_file.read()
            new_song = songs(
                Name=name,
                lyrics=lyrics,
                Artist=nm,
                Albumid=0,
                Genre=genre,
                pics=poster,
                links=mp3_bytes  
            )
            db.session.add(new_song)
            db.session.commit()
            return jsonify({'statusofit': 'ok'})
    
    @app.route("/addsA/<string:nm>",methods=["GET","POST"])
    def addsA(nm):
        if request.method == 'POST':
            print('herererererccxxddegfdgj')
            name = request.form['Name']
            genre = request.form['Genre']
          
            new_song = Album(
                Name=name,
                Artist=nm,
                Genre=genre,
            )
            db.session.add(new_song)
            db.session.commit()
            return jsonify({'statusofit': 'ok'})
    
    @app.route("/addAA/<string:nm>/<int:id>",methods=["GET","POST"])
    def addAA(nm,id):
        if request.method == 'POST':
            print('herererererccxxddegfdgj')
            name = request.form['Name']
            lyrics = request.form['Lyrics']
            genre = request.form['Genre']
            poster = request.form['Poster']
            mp3_file = request.files['song']
            mp3_bytes = mp3_file.read()
            new_song = songs(
                Name=name,
                lyrics=lyrics,
                Artist=nm,
                Albumid=id,
                Genre=genre,
                pics=poster,
                links=mp3_bytes  
            )
            db.session.add(new_song)
            db.session.commit()
            return jsonify({'statusofit': 'ok'})
        
    @app.route("/cc",methods=["GET","POST"])
    def cc():
        x=Users.query.filter(Users.type=='creator').all()
        L=[]
        L = [
               {
                'id': ss.id,
                'Name': ss.name,
            }
            for ss in x
            ]
        return render_template("usera.html",L=L,flag=0,flax=0,str='c')
    
    @app.route("/uu",methods=["GET","POST"])
    def uu():
        x=Users.query.filter(Users.type=='user').all()
        L=[]
        L = [
               {
                'id': ss.id,
                'Name': ss.name,
            }
            for ss in x
            ]
        return render_template("usera.html",L=L,flag=0,flax=0,str='u')    
    @app.route("/tt",methods=["GET","POST"])
    def tt():
        x=songs.query.all()
        L=[]
        L = [
               {
                'id': ss.id,
                'Name': ss.Name,
                'Artist':ss.Artist

            }
            for ss in x
            ]
        return render_template("usera.html",L=L,flag=1,flax=1,str='t')

    @app.route("/aa",methods=["GET","POST"])
    def aa():
        x=Album.query.all()
        L=[]
        L = [
              {
                'id': ss.id,
                'Name': ss.Name,
                'Artist':ss.Artist
            }
            for ss in x
            ] 
        return render_template("usera.html",L=L,flag=0,flax=1,str='a')
    
    @app.route("/remo/<int:id>/<string:str>",methods=["GET","POST"])
    def remo(id,str):
        if str=='a':
            A=Album.query.filter(Album.id==id).first()
            B=songs.query.filter(songs.Albumid==id).all()
            db.session.delete(A)
            db.session.commit()
            for playlist in B:
                db.session.delete(playlist)
            db.session.commit()
            return jsonify({'statusofit': 'ok'})
        elif str =='t':
            A=songs.query.filter(songs.id==id).first()
            db.session.delete(A)
            db.session.commit()
            return jsonify({'statusofit': 'ok'})
        elif str == 'u':
            A=Users.query.filter(Users.id==id).first()
            B=Playlist.query.filter(Playlist.creator==id).all()
            L=[]
            L = [
              {
                'id': ss.id
            }
            for ss in B
            ] 
            C=Playlist.query.filter(PlaylistSongs.playlistid.in_(L)).all()
            for playlist in C:
                db.session.delete(playlist)
            db.session.commit()
            db.session.delete(A)
            db.session.commit()
            for playlist in B:
                db.session.delete(playlist)
            db.session.commit()
            return jsonify({'statusofit': 'ok'})
        elif str=='c':
            A=Users.query.filter(Users.id==id).first()
            nn=A.Name
            B=songs.query.filter(songs.Artist==nn).all()
            C=Album.query.filter(Album.Artist==nn).all()
            for playlist in C:
                db.session.delete(playlist)
            db.session.commit()
            db.session.delete(A)
            db.session.commit()
            for playlist in B:
                db.session.delete(playlist)
            db.session.commit()
            return jsonify({'statusofit': 'ok'})
    @app.route("/recomend/<string:stx>",methods=["GET","POST"])
    def recomend(stx):
        if request.method =='GET':
            print(stx)
            data=ast.literal_eval(stx)
            print(data)
            so = songs.query.filter(songs.id.in_(data)).all()
            L = [
               {
                'id': ss.id,
                'Name': ss.Name,
                'Artist': ss.Artist,
                'pics': ss.pics,
            }
            for ss in so
            ]
            return render_template("play.html", L=L, flag=0, nm="None", id=0)
    
    @app.route("/addCluster/<int:Uid>/<int:Sid>",methods=["GET","POST"])
    def addCluster(Uid,Sid):
        Sd=songs.query.filter(songs.id==Sid).first()
        gnr=Sd.Genre
        U=Cluster.query.filter(Cluster.uid==Uid,Cluster.sid==Sid)
        if U :
            U.count=U.count+1
        else:
            nx=Cluster(uid=Uid,sid=Sid,genre=gnr,count=1)
            db.session.add(nx)
            db.session.commit()

        return jsonify({'statusofit': 'ok'})  
    
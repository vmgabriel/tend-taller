var should = require('chai').should();

describe('User', () => {
  describe('Datos', () => {
    it('Revision que la tabla exista en la base de datos', (done) => {
      User.findAll({})
        .then(datos => {
          datos.should.not.null;
          datos.should.have.lengthOf(10);
          done();
        })
        .catch(e => {
          done(e);
        });
    });

    it('Revision que se puede crear un usuario', (done) => {
      User.create({ name: 'usuario1', passwordHash: 'passwordHasss' })
        .then(() => {
          done();
        })
        .catch(err => {
          done(err);
        });
    });

    it ('Revision que se puede Modificar un Usuario', (done) => {
      User.update({ passwordHash: 'passwordHasss111' }, { where: { name: 'usuario1' } })
        .then(() => {
          done();
        })
        .catch(e => {
          done(e);
        });
    });
    it ('Revision que se puede Eliminar un Usuario', (done) => {
      User.destroy({ where: { name: 'usuario1' } })
        .then(() => {
          done();
        })
        .catch(e => {
          done(e);
        });
    });
  });
});

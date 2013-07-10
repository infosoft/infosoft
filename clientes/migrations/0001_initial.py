# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table(u'clientes_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Categoria'])

        # Adding model 'Pais'
        db.create_table(u'clientes_pais', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Pais'])

        # Adding model 'Estado'
        db.create_table(u'clientes_estado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Pais'])),
        ))
        db.send_create_signal(u'clientes', ['Estado'])

        # Adding model 'Ciudad'
        db.create_table(u'clientes_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Estado'])),
        ))
        db.send_create_signal(u'clientes', ['Ciudad'])

        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('telefonos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Pais'])),
            ('estado', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['clientes.Estado'])),
            ('ciudad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['clientes.Ciudad'])),
            ('ingreso', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])

        # Adding M2M table for field categoria on 'Cliente'
        m2m_table_name = db.shorten_name(u'clientes_cliente_categoria')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cliente', models.ForeignKey(orm[u'clientes.cliente'], null=False)),
            ('categoria', models.ForeignKey(orm[u'clientes.categoria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cliente_id', 'categoria_id'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table(u'clientes_categoria')

        # Deleting model 'Pais'
        db.delete_table(u'clientes_pais')

        # Deleting model 'Estado'
        db.delete_table(u'clientes_estado')

        # Deleting model 'Ciudad'
        db.delete_table(u'clientes_ciudad')

        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')

        # Removing M2M table for field categoria on 'Cliente'
        db.delete_table(db.shorten_name(u'clientes_cliente_categoria'))


    models = {
        u'clientes.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'clientes.ciudad': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Ciudad'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clientes.Categoria']", 'symmetrical': 'False'}),
            'ciudad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['clientes.Ciudad']"}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['clientes.Estado']"}),
            'geo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingreso': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Pais']"}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clientes.estado': {
            'Meta': {'object_name': 'Estado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Pais']"})
        },
        u'clientes.pais': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['clientes']
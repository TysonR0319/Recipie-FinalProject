"""empty message

Revision ID: 645b1cd238f7
Revises: 28af24917ae1
Create Date: 2022-09-02 00:01:22.297235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '645b1cd238f7'
down_revision = '28af24917ae1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('servings', sa.String(), nullable=False),
    sa.Column('ingredients', sa.String(), nullable=False),
    sa.Column('directions', sa.String(), nullable=False),
    sa.Column('credit', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('directions'),
    sa.UniqueConstraint('ingredients'),
    sa.UniqueConstraint('servings'),
    sa.UniqueConstraint('title')
    )
    op.create_table('shopping_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('item', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('recipe_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('username', sa.String(length=30), nullable=False))
    op.add_column('user', sa.Column('firstname', sa.String(), nullable=False))
    op.add_column('user', sa.Column('lastname', sa.String(), nullable=False))
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=20),
               existing_nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.create_unique_constraint(None, 'user', ['username'])
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)
    op.drop_column('user', 'lastname')
    op.drop_column('user', 'firstname')
    op.drop_column('user', 'username')
    op.drop_table('favorite')
    op.drop_table('shopping_list')
    op.drop_table('recipe')
    # ### end Alembic commands ###
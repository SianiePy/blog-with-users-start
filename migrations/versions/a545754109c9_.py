"""empty message

Revision ID: a545754109c9
Revises: 
Create Date: 2021-01-25 20:17:13.003262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a545754109c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_posts', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'blog_posts', 'users', ['author_id'], ['id'])
    op.drop_column('blog_posts', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_posts', sa.Column('author', sa.VARCHAR(length=250), nullable=False))
    op.drop_constraint(None, 'blog_posts', type_='foreignkey')
    op.drop_column('blog_posts', 'author_id')
    # ### end Alembic commands ###

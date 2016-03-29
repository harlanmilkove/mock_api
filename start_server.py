import os

from app.app import app


app.logger.info('Starting server')
app.run(
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 5000)),
    debug=True,
)

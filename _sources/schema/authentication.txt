.. _schema_authentication:

Authentication
==============

We describe a potential method for authenticating :ref:`data store requests <schema_request>` between web client and front-end and back-end servers.

There are two steps to authenticating requests: initial authentication and subsequent request validation.

======================
Initial authentication
======================

The following figure shows the authentication process between the end user's web browser, the front-end server (visualization server), and the Targetscope data back-end server:

.. image:: ../../_static/schema_authentication_flow.png

**Roles**
        1. The *web browser* is the end user's web client for accessing the *front-end* server.
        2. The *front-end* server provides an interface to the data stored on the *back-end* server.
        3. The *back-end* stores and manipulates datacubes etc. and responds to operation requests from the *web browser* and *front-end* clients.

The *front-end* and *back-end* servers share a private key used to sign and validate requests.

**Flow**
        1. The end user's *web browser* lacks a session ID cookie and is presented with a login view. The end user enters her credentials.
        2. The *front-end* web application service validates the credentials against its user database.
        3. If valid, the *front-end* passes a *session ID* cookie back to the *web browser*, which then presents the end user with an authenticated view. The *front-end* also stores the *session ID* and a *timestamp* in a local session database. 

The session ID is subsequently used to handle signing of requests. The session ID is associated with a timestamp, in order to redirect users to reauthenticate if the session is too old.

==================
Request validation
==================

Modeled on `Amazon Web Service request authentication <http://www.faqs.org/rfcs/rfc2104.html>`_, we use `HMAC <http://en.wikipedia.org/wiki/Hash-based_message_authentication_code>`_ to sign requests from the *web browser* with a private key known by the *front-end* and *back-end* servers.

The "signed request" is sent from the *web browser* to the *back-end*, which compares the request's HMAC signature against one it generates. The *back-end* server responds with data, if the signature and timestamp are valid; or, it responds with an authentication error, if the signature is invalid or the request too dated.

.. image:: ../../_static/schema_authentication_request.png

**Flow**
        1. The end user's *web browser* sends an unsigned data request with session ID to the *front-end*.
        2. The *front-end* validates the session ID:

           a. The session ID needs to be in the *front-end* session database. Also, the request timestamp should be within the lifespan of the session ID stored in the FE database. If the session is expired, the end user is redirected to a login view.

           b. If the session ID is valid/live, the request string is encrypted with the *front-end* private key, and hashed with SHA256 to generate an "HMAC signature".

        3. The *front-end* returns the HMAC signature to the *web browser*.
        4. The *web browser* sends the HMAC signature along with the data request's JSON string to the *back-end* server. The HMAC signature is sent as an HTTP header value.
        5. The *back-end* server extracts the HMAC signature value from headers in the HTTP request.
        6. The *back-end* generates a local HMAC signature from the data request JSON string and the FE private key.
        7. If the two HMAC signatures are equivalent, and if the request timestamp is reasonably recent, the request is valid and the *back-end* server sends a response with data results. If the two HMAC messages are different or the request is old, the request is invalid and the *back-end* server sends an authentication error.